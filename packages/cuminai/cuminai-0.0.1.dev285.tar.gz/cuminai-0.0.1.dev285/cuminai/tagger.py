from cuminai.constants import (
    _LINK_KIND,
    _TEXT_KIND
)

import cuminai.utils as utils

class Tagger:
    def __init__(self, chunks, source_kind, tags, **kwargs):
        self._chunks = chunks
        self._sourcekind = source_kind
        self._tags = tags

    def add_global_tags(self):
        if self._sourcekind == _LINK_KIND:
            for chunk in self._chunks:
                for tag in self._tags[chunk.metadata['source']]:
                    chunk.metadata[f'tag-{utils.get_processed_tag(tag)}'] = True
        elif self._sourcekind == _TEXT_KIND:
            for chunk in self._chunks:
                for tag in self._tags[utils.get_file_name(chunk.metadata['source'])]:
                    chunk.metadata[f'tag-{utils.get_processed_tag(tag)}'] = True

    def add_local_tags(self, tag_threshold):
        if self._sourcekind == _LINK_KIND:
            for chunk in self._chunks:
                for tag in self._tags[chunk.metadata['source']]:
                    if utils.num_found(chunk.page_content, tag) >= tag_threshold:
                        chunk.metadata[f'tag-{utils.get_processed_tag(tag)}'] = True
        elif self._sourcekind == _TEXT_KIND:
            for chunk in self._chunks:
                for tag in self._tags[utils.get_file_name(chunk.metadata['source'])]:
                    if utils.num_found(chunk.page_content, tag) >= tag_threshold:
                        chunk.metadata[f'tag-{utils.get_processed_tag(tag)}'] = True

    def get_tagged_chunks(self):
        return self._chunks