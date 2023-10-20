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

try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from openfga_sdk_sync.configuration import Configuration


class RelationMetadata(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'directly_related_user_types': 'list[RelationReference]'
    }

    attribute_map = {
        'directly_related_user_types': 'directly_related_user_types'
    }

    def __init__(self, directly_related_user_types=None, local_vars_configuration=None):  # noqa: E501
        """RelationMetadata - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._directly_related_user_types = None
        self.discriminator = None

        if directly_related_user_types is not None:
            self.directly_related_user_types = directly_related_user_types

    @property
    def directly_related_user_types(self):
        """Gets the directly_related_user_types of this RelationMetadata.  # noqa: E501


        :return: The directly_related_user_types of this RelationMetadata.  # noqa: E501
        :rtype: list[RelationReference]
        """
        return self._directly_related_user_types

    @directly_related_user_types.setter
    def directly_related_user_types(self, directly_related_user_types):
        """Sets the directly_related_user_types of this RelationMetadata.


        :param directly_related_user_types: The directly_related_user_types of this RelationMetadata.  # noqa: E501
        :type directly_related_user_types: list[RelationReference]
        """

        self._directly_related_user_types = directly_related_user_types

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RelationMetadata):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RelationMetadata):
            return True

        return self.to_dict() != other.to_dict()
