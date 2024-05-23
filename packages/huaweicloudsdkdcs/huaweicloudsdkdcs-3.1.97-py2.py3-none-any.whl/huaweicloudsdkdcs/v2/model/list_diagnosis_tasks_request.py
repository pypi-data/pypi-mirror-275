# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDiagnosisTasksRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, instance_id=None, limit=None, offset=None):
        """ListDiagnosisTasksRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param limit: 每页显示条数，最小值为1，最大值为1000，若不设置该参数，则为10。
        :type limit: int
        :param offset: 偏移量，表示从此偏移量开始查询， offset大于等于0。
        :type offset: int
        """
        
        

        self._instance_id = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.instance_id = instance_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def instance_id(self):
        """Gets the instance_id of this ListDiagnosisTasksRequest.

        实例ID

        :return: The instance_id of this ListDiagnosisTasksRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListDiagnosisTasksRequest.

        实例ID

        :param instance_id: The instance_id of this ListDiagnosisTasksRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def limit(self):
        """Gets the limit of this ListDiagnosisTasksRequest.

        每页显示条数，最小值为1，最大值为1000，若不设置该参数，则为10。

        :return: The limit of this ListDiagnosisTasksRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListDiagnosisTasksRequest.

        每页显示条数，最小值为1，最大值为1000，若不设置该参数，则为10。

        :param limit: The limit of this ListDiagnosisTasksRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListDiagnosisTasksRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0。

        :return: The offset of this ListDiagnosisTasksRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListDiagnosisTasksRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0。

        :param offset: The offset of this ListDiagnosisTasksRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListDiagnosisTasksRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
