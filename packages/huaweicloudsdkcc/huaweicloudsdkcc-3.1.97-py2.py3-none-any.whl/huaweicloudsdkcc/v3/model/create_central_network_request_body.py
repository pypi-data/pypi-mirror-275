# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateCentralNetworkRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'central_network': 'CreateCentralNetwork'
    }

    attribute_map = {
        'central_network': 'central_network'
    }

    def __init__(self, central_network=None):
        """CreateCentralNetworkRequestBody

        The model defined in huaweicloud sdk

        :param central_network: 
        :type central_network: :class:`huaweicloudsdkcc.v3.CreateCentralNetwork`
        """
        
        

        self._central_network = None
        self.discriminator = None

        self.central_network = central_network

    @property
    def central_network(self):
        """Gets the central_network of this CreateCentralNetworkRequestBody.

        :return: The central_network of this CreateCentralNetworkRequestBody.
        :rtype: :class:`huaweicloudsdkcc.v3.CreateCentralNetwork`
        """
        return self._central_network

    @central_network.setter
    def central_network(self, central_network):
        """Sets the central_network of this CreateCentralNetworkRequestBody.

        :param central_network: The central_network of this CreateCentralNetworkRequestBody.
        :type central_network: :class:`huaweicloudsdkcc.v3.CreateCentralNetwork`
        """
        self._central_network = central_network

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateCentralNetworkRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
