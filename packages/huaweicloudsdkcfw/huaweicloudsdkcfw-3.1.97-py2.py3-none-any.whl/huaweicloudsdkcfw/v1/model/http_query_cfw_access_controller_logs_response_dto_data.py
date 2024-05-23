# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HttpQueryCfwAccessControllerLogsResponseDTOData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'limit': 'int',
        'records': 'list[HttpQueryCfwAccessControllerLogsResponseDTODataRecords]'
    }

    attribute_map = {
        'total': 'total',
        'limit': 'limit',
        'records': 'records'
    }

    def __init__(self, total=None, limit=None, records=None):
        """HttpQueryCfwAccessControllerLogsResponseDTOData

        The model defined in huaweicloud sdk

        :param total: 返回数量
        :type total: int
        :param limit: 每页显示个数，范围为1-1024
        :type limit: int
        :param records: 记录
        :type records: list[:class:`huaweicloudsdkcfw.v1.HttpQueryCfwAccessControllerLogsResponseDTODataRecords`]
        """
        
        

        self._total = None
        self._limit = None
        self._records = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if limit is not None:
            self.limit = limit
        if records is not None:
            self.records = records

    @property
    def total(self):
        """Gets the total of this HttpQueryCfwAccessControllerLogsResponseDTOData.

        返回数量

        :return: The total of this HttpQueryCfwAccessControllerLogsResponseDTOData.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this HttpQueryCfwAccessControllerLogsResponseDTOData.

        返回数量

        :param total: The total of this HttpQueryCfwAccessControllerLogsResponseDTOData.
        :type total: int
        """
        self._total = total

    @property
    def limit(self):
        """Gets the limit of this HttpQueryCfwAccessControllerLogsResponseDTOData.

        每页显示个数，范围为1-1024

        :return: The limit of this HttpQueryCfwAccessControllerLogsResponseDTOData.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this HttpQueryCfwAccessControllerLogsResponseDTOData.

        每页显示个数，范围为1-1024

        :param limit: The limit of this HttpQueryCfwAccessControllerLogsResponseDTOData.
        :type limit: int
        """
        self._limit = limit

    @property
    def records(self):
        """Gets the records of this HttpQueryCfwAccessControllerLogsResponseDTOData.

        记录

        :return: The records of this HttpQueryCfwAccessControllerLogsResponseDTOData.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.HttpQueryCfwAccessControllerLogsResponseDTODataRecords`]
        """
        return self._records

    @records.setter
    def records(self, records):
        """Sets the records of this HttpQueryCfwAccessControllerLogsResponseDTOData.

        记录

        :param records: The records of this HttpQueryCfwAccessControllerLogsResponseDTOData.
        :type records: list[:class:`huaweicloudsdkcfw.v1.HttpQueryCfwAccessControllerLogsResponseDTODataRecords`]
        """
        self._records = records

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
        if not isinstance(other, HttpQueryCfwAccessControllerLogsResponseDTOData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
