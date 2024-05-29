import asyncio

from cuminai.constants import (
    _DEFAULT_CHUNK_SIZE,
    _DEFAULT_CHUNK_OVERLAP,
)

from langchain_text_splitters import CharacterTextSplitter

class Chunker:
    def __init__(self, **kwargs):
        self._docs = kwargs.get('docs', [])
        self._chunk_size = kwargs.get('chunk_size', _DEFAULT_CHUNK_SIZE)
        self._chunk_overlap = kwargs.get('chunk_overlap', _DEFAULT_CHUNK_OVERLAP)

    def get_chunks(self):
        text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
            chunk_size=self._chunk_size, chunk_overlap=self._chunk_overlap
        )

        return text_splitter.split_documents(self._docs)