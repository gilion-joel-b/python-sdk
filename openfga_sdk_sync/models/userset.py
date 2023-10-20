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


class Userset(object):
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
        'this': 'object',
        'computed_userset': 'ObjectRelation',
        'tuple_to_userset': 'TupleToUserset',
        'union': 'Usersets',
        'intersection': 'Usersets',
        'difference': 'Difference'
    }

    attribute_map = {
        'this': 'this',
        'computed_userset': 'computedUserset',
        'tuple_to_userset': 'tupleToUserset',
        'union': 'union',
        'intersection': 'intersection',
        'difference': 'difference'
    }

    def __init__(self, this=None, computed_userset=None, tuple_to_userset=None, union=None, intersection=None, difference=None, local_vars_configuration=None):  # noqa: E501
        """Userset - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._this = None
        self._computed_userset = None
        self._tuple_to_userset = None
        self._union = None
        self._intersection = None
        self._difference = None
        self.discriminator = None

        if this is not None:
            self.this = this
        if computed_userset is not None:
            self.computed_userset = computed_userset
        if tuple_to_userset is not None:
            self.tuple_to_userset = tuple_to_userset
        if union is not None:
            self.union = union
        if intersection is not None:
            self.intersection = intersection
        if difference is not None:
            self.difference = difference

    @property
    def this(self):
        """Gets the this of this Userset.  # noqa: E501

        A DirectUserset is a sentinel message for referencing the direct members specified by an object/relation mapping.  # noqa: E501

        :return: The this of this Userset.  # noqa: E501
        :rtype: object
        """
        return self._this

    @this.setter
    def this(self, this):
        """Sets the this of this Userset.

        A DirectUserset is a sentinel message for referencing the direct members specified by an object/relation mapping.  # noqa: E501

        :param this: The this of this Userset.  # noqa: E501
        :type this: object
        """

        self._this = this

    @property
    def computed_userset(self):
        """Gets the computed_userset of this Userset.  # noqa: E501


        :return: The computed_userset of this Userset.  # noqa: E501
        :rtype: ObjectRelation
        """
        return self._computed_userset

    @computed_userset.setter
    def computed_userset(self, computed_userset):
        """Sets the computed_userset of this Userset.


        :param computed_userset: The computed_userset of this Userset.  # noqa: E501
        :type computed_userset: ObjectRelation
        """

        self._computed_userset = computed_userset

    @property
    def tuple_to_userset(self):
        """Gets the tuple_to_userset of this Userset.  # noqa: E501


        :return: The tuple_to_userset of this Userset.  # noqa: E501
        :rtype: TupleToUserset
        """
        return self._tuple_to_userset

    @tuple_to_userset.setter
    def tuple_to_userset(self, tuple_to_userset):
        """Sets the tuple_to_userset of this Userset.


        :param tuple_to_userset: The tuple_to_userset of this Userset.  # noqa: E501
        :type tuple_to_userset: TupleToUserset
        """

        self._tuple_to_userset = tuple_to_userset

    @property
    def union(self):
        """Gets the union of this Userset.  # noqa: E501


        :return: The union of this Userset.  # noqa: E501
        :rtype: Usersets
        """
        return self._union

    @union.setter
    def union(self, union):
        """Sets the union of this Userset.


        :param union: The union of this Userset.  # noqa: E501
        :type union: Usersets
        """

        self._union = union

    @property
    def intersection(self):
        """Gets the intersection of this Userset.  # noqa: E501


        :return: The intersection of this Userset.  # noqa: E501
        :rtype: Usersets
        """
        return self._intersection

    @intersection.setter
    def intersection(self, intersection):
        """Sets the intersection of this Userset.


        :param intersection: The intersection of this Userset.  # noqa: E501
        :type intersection: Usersets
        """

        self._intersection = intersection

    @property
    def difference(self):
        """Gets the difference of this Userset.  # noqa: E501


        :return: The difference of this Userset.  # noqa: E501
        :rtype: Difference
        """
        return self._difference

    @difference.setter
    def difference(self, difference):
        """Sets the difference of this Userset.


        :param difference: The difference of this Userset.  # noqa: E501
        :type difference: Difference
        """

        self._difference = difference

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
        if not isinstance(other, Userset):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Userset):
            return True

        return self.to_dict() != other.to_dict()
