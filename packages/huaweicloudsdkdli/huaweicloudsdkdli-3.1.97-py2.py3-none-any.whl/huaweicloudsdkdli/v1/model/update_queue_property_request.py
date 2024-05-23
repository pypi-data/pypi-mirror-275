# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateQueuePropertyRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'queue_name': 'str',
        'body': 'UpdateQueuePropertyRequestBody'
    }

    attribute_map = {
        'queue_name': 'queue_name',
        'body': 'body'
    }

    def __init__(self, queue_name=None, body=None):
        """UpdateQueuePropertyRequest

        The model defined in huaweicloud sdk

        :param queue_name: 队列名称
        :type queue_name: str
        :param body: Body of the UpdateQueuePropertyRequest
        :type body: :class:`huaweicloudsdkdli.v1.UpdateQueuePropertyRequestBody`
        """
        
        

        self._queue_name = None
        self._body = None
        self.discriminator = None

        self.queue_name = queue_name
        if body is not None:
            self.body = body

    @property
    def queue_name(self):
        """Gets the queue_name of this UpdateQueuePropertyRequest.

        队列名称

        :return: The queue_name of this UpdateQueuePropertyRequest.
        :rtype: str
        """
        return self._queue_name

    @queue_name.setter
    def queue_name(self, queue_name):
        """Sets the queue_name of this UpdateQueuePropertyRequest.

        队列名称

        :param queue_name: The queue_name of this UpdateQueuePropertyRequest.
        :type queue_name: str
        """
        self._queue_name = queue_name

    @property
    def body(self):
        """Gets the body of this UpdateQueuePropertyRequest.

        :return: The body of this UpdateQueuePropertyRequest.
        :rtype: :class:`huaweicloudsdkdli.v1.UpdateQueuePropertyRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateQueuePropertyRequest.

        :param body: The body of this UpdateQueuePropertyRequest.
        :type body: :class:`huaweicloudsdkdli.v1.UpdateQueuePropertyRequestBody`
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
        if not isinstance(other, UpdateQueuePropertyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
