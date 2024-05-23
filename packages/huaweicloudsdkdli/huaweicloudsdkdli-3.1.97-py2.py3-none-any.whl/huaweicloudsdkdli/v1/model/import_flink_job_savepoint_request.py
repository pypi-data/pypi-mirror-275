# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImportFlinkJobSavepointRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'body': 'ImportFlinkJobSavepointRequestBody'
    }

    attribute_map = {
        'job_id': 'job_id',
        'body': 'body'
    }

    def __init__(self, job_id=None, body=None):
        """ImportFlinkJobSavepointRequest

        The model defined in huaweicloud sdk

        :param job_id: 非运行阶段的Flink作业的作业ID
        :type job_id: str
        :param body: Body of the ImportFlinkJobSavepointRequest
        :type body: :class:`huaweicloudsdkdli.v1.ImportFlinkJobSavepointRequestBody`
        """
        
        

        self._job_id = None
        self._body = None
        self.discriminator = None

        self.job_id = job_id
        if body is not None:
            self.body = body

    @property
    def job_id(self):
        """Gets the job_id of this ImportFlinkJobSavepointRequest.

        非运行阶段的Flink作业的作业ID

        :return: The job_id of this ImportFlinkJobSavepointRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ImportFlinkJobSavepointRequest.

        非运行阶段的Flink作业的作业ID

        :param job_id: The job_id of this ImportFlinkJobSavepointRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def body(self):
        """Gets the body of this ImportFlinkJobSavepointRequest.

        :return: The body of this ImportFlinkJobSavepointRequest.
        :rtype: :class:`huaweicloudsdkdli.v1.ImportFlinkJobSavepointRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ImportFlinkJobSavepointRequest.

        :param body: The body of this ImportFlinkJobSavepointRequest.
        :type body: :class:`huaweicloudsdkdli.v1.ImportFlinkJobSavepointRequestBody`
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
        if not isinstance(other, ImportFlinkJobSavepointRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
