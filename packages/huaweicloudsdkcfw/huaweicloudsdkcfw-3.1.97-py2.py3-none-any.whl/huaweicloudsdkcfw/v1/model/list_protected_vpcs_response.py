# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListProtectedVpcsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'trace_id': 'str',
        'data': 'VPCProtectsVo'
    }

    attribute_map = {
        'trace_id': 'trace_id',
        'data': 'data'
    }

    def __init__(self, trace_id=None, data=None):
        """ListProtectedVpcsResponse

        The model defined in huaweicloud sdk

        :param trace_id: 调用链id
        :type trace_id: str
        :param data: 
        :type data: :class:`huaweicloudsdkcfw.v1.VPCProtectsVo`
        """
        
        super(ListProtectedVpcsResponse, self).__init__()

        self._trace_id = None
        self._data = None
        self.discriminator = None

        if trace_id is not None:
            self.trace_id = trace_id
        if data is not None:
            self.data = data

    @property
    def trace_id(self):
        """Gets the trace_id of this ListProtectedVpcsResponse.

        调用链id

        :return: The trace_id of this ListProtectedVpcsResponse.
        :rtype: str
        """
        return self._trace_id

    @trace_id.setter
    def trace_id(self, trace_id):
        """Sets the trace_id of this ListProtectedVpcsResponse.

        调用链id

        :param trace_id: The trace_id of this ListProtectedVpcsResponse.
        :type trace_id: str
        """
        self._trace_id = trace_id

    @property
    def data(self):
        """Gets the data of this ListProtectedVpcsResponse.

        :return: The data of this ListProtectedVpcsResponse.
        :rtype: :class:`huaweicloudsdkcfw.v1.VPCProtectsVo`
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ListProtectedVpcsResponse.

        :param data: The data of this ListProtectedVpcsResponse.
        :type data: :class:`huaweicloudsdkcfw.v1.VPCProtectsVo`
        """
        self._data = data

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
        if not isinstance(other, ListProtectedVpcsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
