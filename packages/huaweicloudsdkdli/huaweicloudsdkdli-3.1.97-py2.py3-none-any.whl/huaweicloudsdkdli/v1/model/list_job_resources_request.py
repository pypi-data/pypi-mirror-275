# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListJobResourcesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'kind': 'str',
        'tags': 'str'
    }

    attribute_map = {
        'kind': 'kind',
        'tags': 'tags'
    }

    def __init__(self, kind=None, tags=None):
        """ListJobResourcesRequest

        The model defined in huaweicloud sdk

        :param kind: 
        :type kind: str
        :param tags: 
        :type tags: str
        """
        
        

        self._kind = None
        self._tags = None
        self.discriminator = None

        if kind is not None:
            self.kind = kind
        if tags is not None:
            self.tags = tags

    @property
    def kind(self):
        """Gets the kind of this ListJobResourcesRequest.

        :return: The kind of this ListJobResourcesRequest.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this ListJobResourcesRequest.

        :param kind: The kind of this ListJobResourcesRequest.
        :type kind: str
        """
        self._kind = kind

    @property
    def tags(self):
        """Gets the tags of this ListJobResourcesRequest.

        :return: The tags of this ListJobResourcesRequest.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ListJobResourcesRequest.

        :param tags: The tags of this ListJobResourcesRequest.
        :type tags: str
        """
        self._tags = tags

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
        if not isinstance(other, ListJobResourcesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
