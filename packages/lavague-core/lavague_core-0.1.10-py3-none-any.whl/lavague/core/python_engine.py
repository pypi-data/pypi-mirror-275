"""Note: We used to have a version of this that was quite flexible and could allow for others to provide their capabilities and the Python engine could use them.
However, we have decided to simplify the Python engine to only use the LLM and Embedding from the context for the moment as the Python Engine we want is a bit complex.
We will revisit this in the future to be able to have both:
- Capabilities that can be provided by others
- State management that can allow a complex agentic workflow"""

from lavague.core.context import Context, get_default_context
from llama_index.core.base.llms.base import BaseLLM
from llama_index.core.embeddings import BaseEmbedding

import trafilatura
from llama_index.core import Document, VectorStoreIndex


class PythonEngine:
    llm: BaseLLM
    embedding: BaseEmbedding

    def __init__(
        self,
        llm: BaseLLM = get_default_context().llm,
        embedding: BaseEmbedding = get_default_context().embedding,
    ):
        self.llm = llm
        self.embedding = embedding

    @classmethod
    def from_context(
        cls,
        context: Context,
    ):
        return cls(context.llm, context.embedding)

    def extract_information(self, instruction: str, html: str) -> str:
        llm = self.llm
        embedding = self.embedding

        page_content = trafilatura.extract(html)
        # Next we will use Llama Index to perform RAG on the extracted text content

        documents = [Document(text=page_content)]

        # We then build index
        index = VectorStoreIndex.from_documents(documents, embed_model=embedding)
        query_engine = index.as_query_engine(llm=llm)

        # We finally store the output in the variable 'output'
        output = query_engine.query(instruction).response

        return output
