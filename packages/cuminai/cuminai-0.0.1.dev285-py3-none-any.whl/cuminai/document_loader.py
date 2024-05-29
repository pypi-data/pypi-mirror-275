import asyncio

from langchain_community.document_loaders import WebBaseLoader, TextLoader

def background(f):
    def wrapped(*args, **kwargs):
        return asyncio.get_event_loop().run_in_executor(None, f, *args, **kwargs)
    return wrapped

class Loader:
    def __init__(self, **kwargs):
        self._sources = kwargs.get('sources', [])

    def get_link_docs(self):
        return asyncio.run(self._aload_link_docs())
    
    def get_text_docs(self):
        return asyncio.run(self._aload_text_docs())
    
    async def _aload_link_docs(self):
        docs = [self._aload_link_doc(url) for url in self._sources]
        docs_list = [item for sublist in await asyncio.gather(*docs) for item in sublist]
        return docs_list
    
    async def _aload_text_docs(self):
        docs = [self._aload_text_doc(file) for file in self._sources]
        docs_list = [item for sublist in await asyncio.gather(*docs) for item in sublist]
        return docs_list
    
    @background
    def _aload_link_doc(self, url):
        return WebBaseLoader(url).load()
    
    @background
    def _aload_text_doc(self, filename):
        return TextLoader(f"./{filename}", autodetect_encoding=True).load()