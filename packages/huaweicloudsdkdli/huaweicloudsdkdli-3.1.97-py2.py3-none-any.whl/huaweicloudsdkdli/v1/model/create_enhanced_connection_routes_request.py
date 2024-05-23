# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateEnhancedConnectionRoutesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'connection_id': 'str',
        'body': 'CreateEnhancedConnectionRoutesRequestBody'
    }

    attribute_map = {
        'connection_id': 'connection_id',
        'body': 'body'
    }

    def __init__(self, connection_id=None, body=None):
        """CreateEnhancedConnectionRoutesRequest

        The model defined in huaweicloud sdk

        :param connection_id: 连接ID，用于标识跨源连接的UUID。
        :type connection_id: str
        :param body: Body of the CreateEnhancedConnectionRoutesRequest
        :type body: :class:`huaweicloudsdkdli.v1.CreateEnhancedConnectionRoutesRequestBody`
        """
        
        

        self._connection_id = None
        self._body = None
        self.discriminator = None

        self.connection_id = connection_id
        if body is not None:
            self.body = body

    @property
    def connection_id(self):
        """Gets the connection_id of this CreateEnhancedConnectionRoutesRequest.

        连接ID，用于标识跨源连接的UUID。

        :return: The connection_id of this CreateEnhancedConnectionRoutesRequest.
        :rtype: str
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        """Sets the connection_id of this CreateEnhancedConnectionRoutesRequest.

        连接ID，用于标识跨源连接的UUID。

        :param connection_id: The connection_id of this CreateEnhancedConnectionRoutesRequest.
        :type connection_id: str
        """
        self._connection_id = connection_id

    @property
    def body(self):
        """Gets the body of this CreateEnhancedConnectionRoutesRequest.

        :return: The body of this CreateEnhancedConnectionRoutesRequest.
        :rtype: :class:`huaweicloudsdkdli.v1.CreateEnhancedConnectionRoutesRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CreateEnhancedConnectionRoutesRequest.

        :param body: The body of this CreateEnhancedConnectionRoutesRequest.
        :type body: :class:`huaweicloudsdkdli.v1.CreateEnhancedConnectionRoutesRequestBody`
        """
        self._body = body

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
        if not isinstance(other, CreateEnhancedConnectionRoutesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
