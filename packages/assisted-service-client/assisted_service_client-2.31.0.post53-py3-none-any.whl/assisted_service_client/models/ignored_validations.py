# coding: utf-8

"""
    AssistedInstall

    Assisted installation  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class IgnoredValidations(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'cluster_validation_ids': 'str',
        'host_validation_ids': 'str'
    }

    attribute_map = {
        'cluster_validation_ids': 'cluster-validation-ids',
        'host_validation_ids': 'host-validation-ids'
    }

    def __init__(self, cluster_validation_ids=None, host_validation_ids=None):  # noqa: E501
        """IgnoredValidations - a model defined in Swagger"""  # noqa: E501

        self._cluster_validation_ids = None
        self._host_validation_ids = None
        self.discriminator = None

        if cluster_validation_ids is not None:
            self.cluster_validation_ids = cluster_validation_ids
        if host_validation_ids is not None:
            self.host_validation_ids = host_validation_ids

    @property
    def cluster_validation_ids(self):
        """Gets the cluster_validation_ids of this IgnoredValidations.  # noqa: E501

        JSON-formatted list of cluster validation IDs that will be ignored for all hosts that belong to this cluster. It may also contain a list with a single string \"all\" to ignore all cluster validations. Some validations cannot be ignored.  # noqa: E501

        :return: The cluster_validation_ids of this IgnoredValidations.  # noqa: E501
        :rtype: str
        """
        return self._cluster_validation_ids

    @cluster_validation_ids.setter
    def cluster_validation_ids(self, cluster_validation_ids):
        """Sets the cluster_validation_ids of this IgnoredValidations.

        JSON-formatted list of cluster validation IDs that will be ignored for all hosts that belong to this cluster. It may also contain a list with a single string \"all\" to ignore all cluster validations. Some validations cannot be ignored.  # noqa: E501

        :param cluster_validation_ids: The cluster_validation_ids of this IgnoredValidations.  # noqa: E501
        :type: str
        """

        self._cluster_validation_ids = cluster_validation_ids

    @property
    def host_validation_ids(self):
        """Gets the host_validation_ids of this IgnoredValidations.  # noqa: E501

        JSON-formatted list of host validation IDs that will be ignored for all hosts that belong to this cluster. It may also contain a list with a single string \"all\" to ignore all host validations. Some validations cannot be ignored.  # noqa: E501

        :return: The host_validation_ids of this IgnoredValidations.  # noqa: E501
        :rtype: str
        """
        return self._host_validation_ids

    @host_validation_ids.setter
    def host_validation_ids(self, host_validation_ids):
        """Sets the host_validation_ids of this IgnoredValidations.

        JSON-formatted list of host validation IDs that will be ignored for all hosts that belong to this cluster. It may also contain a list with a single string \"all\" to ignore all host validations. Some validations cannot be ignored.  # noqa: E501

        :param host_validation_ids: The host_validation_ids of this IgnoredValidations.  # noqa: E501
        :type: str
        """

        self._host_validation_ids = host_validation_ids

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(IgnoredValidations, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, IgnoredValidations):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
