# coding: utf-8
"""
   Python SDK for OpenFGA

   API version: 0.1
   Website: https://openfga.dev
   Documentation: https://openfga.dev/docs
   Support: https://discord.gg/8naAwJfWN6
   License: [Apache-2.0](https://github.com/openfga/python-sdk/blob/main/LICENSE)

   NOTE: This file was auto generated by OpenAPI Generator (https://openapi-generator.tech). DO NOT EDIT.
"""


class WriteTransactionOpts:
    """
    OpenFGA client write transaction info
    """

    def __init__(self, disabled: bool = False, max_per_chunk: int = 1, max_parallel_requests: int = 10):
        self._disabled = disabled
        self._max_per_chunk = max_per_chunk
        self._max_parallel_requests = max_parallel_requests

    @property
    def disabled(self):
        """
        Return disabled
        """
        return self._disabled

    @property
    def max_per_chunk(self):
        """
        Return max per chunk
        """
        return self._max_per_chunk

    @property
    def max_parallel_requests(self):
        """
        Return max parallel requests
        """
        return self._max_parallel_requests

    @disabled.setter
    def disabled(self, value):
        """
        Set disabled
        """
        self._disabled = value

    @max_per_chunk.setter
    def max_per_chunk(self, value):
        """
        Set max_per_chunk
        """
        self._max_per_chunk = value

    @max_parallel_requests.setter
    def max_parallel_requests(self, value):
        """
        Set max_parallel_requests
        """
        self._max_parallel_requests = value
