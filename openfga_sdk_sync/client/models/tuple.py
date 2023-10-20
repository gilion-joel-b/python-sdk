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

from openfga_sdk_sync.models.tuple_key import TupleKey

from typing import List


class ClientTuple():
    """
    ClientTuple encapsulates the client tuple
    """

    def __init__(self, user: str, relation: str, object: str):
        self._user = user
        self._relation = relation
        self._object = object

    def __eq__(self, other):
        return self.user == other.user and self.relation == other.relation and self.object == other.object

    @property
    def user(self):
        """
        Return user
        """
        return self._user

    @property
    def relation(self):
        """
        Return relation
        """
        return self._relation

    @property
    def object(self):
        """
        Return object
        """
        return self._object

    @user.setter
    def user(self, value):
        """
        Set user
        """
        self._user = value

    @relation.setter
    def relation(self, value):
        """
        Set relation
        """
        self._relation = value

    @object.setter
    def object(self, value):
        """
        Set object
        """
        self._object = value

    @property
    def tuple_key(self):
        """
        Return the tuple as tuple_key
        """
        return TupleKey(
            object=self.object,
            relation=self.relation,
            user=self.user,
        )


def convert_tuple_keys(lists: List[ClientTuple]):
    """
    Return the items as tuple_keys
    """
    if lists is None:
        return None
    items = map(lambda item: item.tuple_key, lists)
    return list(items)
