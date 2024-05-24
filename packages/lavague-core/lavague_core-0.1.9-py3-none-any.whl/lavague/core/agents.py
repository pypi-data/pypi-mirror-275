import yaml
import time
import uuid
from PIL import Image
from lavague.core.utilities.telemetry import send_telemetry, send_telemetry_scr
from pathlib import Path
from llama_index.core import SimpleDirectoryReader
from lavague.core.action_engine import ActionEngine
from lavague.core.python_engine import PythonEngine
from lavague.core.world_model import WorldModel
from lavague.core.navigation import NavigationControl
from lavague.core.utilities.format_utils import (
    extract_next_engine,
    extract_world_model_instruction,
)
from lavague.core.utilities.web_utils import display_screenshot, get_highlighted_element

try:
    from selenium.webdriver.remote.webdriver import WebDriver
except ImportError:
    raise ImportError(
        "`lavague-drivers-selenium` package not found, "
        "please run `pip install lavague-drivers-selenium`"
    )


class WebAgent:
    """
    Web agent class, for now only works with selenium.
    """

    def __init__(
        self,
        world_model: WorldModel,
        action_engine: ActionEngine,
        python_engine: PythonEngine,
        n_attempts: int = 5,
        n_steps: int = 10,
        time_between_actions: float = 1.5,
    ):
        self.driver: WebDriver = action_engine.driver.get_driver()
        self.action_engine: ActionEngine = action_engine
        self.world_model: WorldModel = world_model
        self.navigation_control: NavigationControl = NavigationControl(self.driver)
        self.python_engine: PythonEngine = python_engine

        self.n_attempts = n_attempts
        self.n_steps = n_steps
        self.time_between_actions = time_between_actions

    def get(self, url):
        self.driver.get(url)

    def run(self, objective: str, user_data=None, display: bool = False):
        world_model = self.world_model
        action_engine = self.action_engine
        python_engine = self.python_engine
        navigation_control = self.navigation_control

        n_steps = self.n_steps
        n_attempts = self.n_attempts
        time_between_actions = self.time_between_actions

        screenshot_path = "screenshots/output.png"

        previous_instructions = "[NONE]"
        last_engine = "[NONE]"

        current_state = {
            "external_observations": {
                "vision": "[SCREEENSHOT]",
            },
            "internal_state": {
                "user_inputs": [],
                "agent_outputs": [],
            },
        }

        run_id = str(uuid.uuid4())

        if user_data:
            current_state["internal_state"]["user_inputs"].append(user_data)

        # TO DO: Don't save on disk the screenshot but do it in memory
        Path("./screenshots").mkdir(exist_ok=True)
        self.driver.save_screenshot(screenshot_path)
        screenshot_before_action = Image.open(screenshot_path)
        if display:
            display_screenshot(screenshot_before_action)
        image_documents = SimpleDirectoryReader("./screenshots").load_data()

        for _ in range(n_steps):
            step_id = str(uuid.uuid4())
            success = True
            error = ""
            bounding_box = {"": 0}
            viewport_size = {"": 0}
            current_state_str = yaml.dump(current_state, default_flow_style=False)

            world_model_output = world_model.get_instruction(
                objective,
                previous_instructions,
                last_engine,
                current_state_str,
                image_documents,
            )

            print(world_model_output)

            next_engine = extract_next_engine(world_model_output)
            instruction = extract_world_model_instruction(world_model_output)

            if next_engine == "Navigation Engine":
                query = instruction
                nodes = action_engine.get_nodes(query)
                llm_context = "\n".join(nodes)

                success = False

                for _ in range(n_attempts):
                    try:
                        image = None
                        screenshot_after_action = None
                        error = ""
                        url = self.driver.current_url
                        success = True
                        action = action_engine.get_action_from_context(
                            llm_context, query
                        )
                        outputs = get_highlighted_element(self.driver, action)
                        image = outputs[-1]["image"]
                        bounding_box = outputs[-1]["bounding_box"]
                        viewport_size = outputs[-1]["viewport_size"]

                        if display:
                            display_screenshot(image)
                        action_code = f"""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
{action}"""
                        local_scope = {"driver": self.driver}
                        exec(action_code, local_scope, local_scope)
                        time.sleep(time_between_actions)
                        self.driver.save_screenshot(screenshot_path)
                        screenshot_before_action = screenshot_after_action
                        screenshot_after_action = Image.open(screenshot_path)
                        if display:
                            display_screenshot(screenshot_after_action)
                        success = True
                        break
                    except Exception as e:
                        print(f"Action execution failed. Retrying...")
                        print("Error: ", e)
                        screenshot_after_action = None
                        image = None
                        error = repr(e)
                    finally:
                        action_id = str(uuid.uuid4())
                        send_telemetry(
                            model_name=action_engine.llm.metadata.model_name,
                            code=action,
                            instruction=instruction,
                            url=url,
                            origin="Agent",
                            success=success,
                            test=False,
                            error=error,
                            source_nodes=llm_context,
                            bounding_box=bounding_box,
                            viewport_size=viewport_size,
                            main_objective=objective,
                            objectives=world_model_output,
                            action_id=action_id,
                            multi_modal_model=world_model.mm_llm.metadata.model_name,
                            step_id=step_id,
                            run_id=run_id,
                        )
                        send_telemetry_scr(
                            action_id,
                            screenshot_before_action,
                            image,
                            screenshot_after_action,
                        )
                if not success:
                    instruction = "[FAILED] " + instruction
                image_documents = SimpleDirectoryReader("./screenshots").load_data()

            elif "Python Engine" in next_engine:
                html = self.driver.page_source
                output = python_engine.extract_information(instruction, html)
                if output:
                    current_state["internal_state"]["agent_outputs"].append(output)

            elif "Navigation Controls" in next_engine:
                navigation_control.execute_instruction(instruction)
                self.driver.save_screenshot(screenshot_path)

                screenshot_after_action = Image.open(screenshot_path)
                if display:
                    display_screenshot(screenshot_after_action)
                image_documents = SimpleDirectoryReader("./screenshots").load_data()

            elif next_engine == "STOP" or instruction == "STOP":
                print("Objective reached. Stopping...")
                break

            if previous_instructions == "[NONE]":
                previous_instructions = f"""
- {instruction}"""
            else:
                previous_instructions += f"""
- {instruction}"""

            last_engine = next_engine

        output = current_state["internal_state"]["agent_outputs"]
        return output
