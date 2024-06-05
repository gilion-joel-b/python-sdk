"""
   Python SDK for OpenFGA

   API version: 1.x
   Website: https://openfga.dev
   Documentation: https://openfga.dev/docs
   Support: https://openfga.dev/community
   License: [Apache-2.0](https://github.com/openfga/python-sdk/blob/main/LICENSE)

   NOTE: This file was auto generated by OpenAPI Generator (https://openapi-generator.tech). DO NOT EDIT.
"""

try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint

from openfga_sdk.configuration import Configuration


class ListStoresResponse:
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
    openapi_types = {"stores": "list[Store]", "continuation_token": "str"}

    attribute_map = {"stores": "stores", "continuation_token": "continuation_token"}

    def __init__(
        self, stores=None, continuation_token=None, local_vars_configuration=None
    ):
        """ListStoresResponse - a model defined in OpenAPI"""
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._stores = None
        self._continuation_token = None
        self.discriminator = None

        self.stores = stores
        self.continuation_token = continuation_token

    @property
    def stores(self):
        """Gets the stores of this ListStoresResponse.


        :return: The stores of this ListStoresResponse.
        :rtype: list[Store]
        """
        return self._stores

    @stores.setter
    def stores(self, stores):
        """Sets the stores of this ListStoresResponse.


        :param stores: The stores of this ListStoresResponse.
        :type stores: list[Store]
        """
        if self.local_vars_configuration.client_side_validation and stores is None:
            raise ValueError("Invalid value for `stores`, must not be `None`")

        self._stores = stores

    @property
    def continuation_token(self):
        """Gets the continuation_token of this ListStoresResponse.

        The continuation token will be empty if there are no more stores.

        :return: The continuation_token of this ListStoresResponse.
        :rtype: str
        """
        return self._continuation_token

    @continuation_token.setter
    def continuation_token(self, continuation_token):
        """Sets the continuation_token of this ListStoresResponse.

        The continuation token will be empty if there are no more stores.

        :param continuation_token: The continuation_token of this ListStoresResponse.
        :type continuation_token: str
        """
        if (
            self.local_vars_configuration.client_side_validation
            and continuation_token is None
        ):
            raise ValueError(
                "Invalid value for `continuation_token`, must not be `None`"
            )

        self._continuation_token = continuation_token

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

        for attr, _ in self.openapi_types.items():
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(lambda x: convert(x), value))
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(lambda item: (item[0], convert(item[1])), value.items())
                )
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
        if not isinstance(other, ListStoresResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListStoresResponse):
            return True

        return self.to_dict() != other.to_dict()
