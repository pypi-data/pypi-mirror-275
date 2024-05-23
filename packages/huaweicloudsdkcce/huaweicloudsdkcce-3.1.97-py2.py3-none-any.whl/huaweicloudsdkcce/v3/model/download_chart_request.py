# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DownloadChartRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'chart_id': 'str'
    }

    attribute_map = {
        'chart_id': 'chart_id'
    }

    def __init__(self, chart_id=None):
        """DownloadChartRequest

        The model defined in huaweicloud sdk

        :param chart_id: 模板的ID
        :type chart_id: str
        """
        
        

        self._chart_id = None
        self.discriminator = None

        self.chart_id = chart_id

    @property
    def chart_id(self):
        """Gets the chart_id of this DownloadChartRequest.

        模板的ID

        :return: The chart_id of this DownloadChartRequest.
        :rtype: str
        """
        return self._chart_id

    @chart_id.setter
    def chart_id(self, chart_id):
        """Sets the chart_id of this DownloadChartRequest.

        模板的ID

        :param chart_id: The chart_id of this DownloadChartRequest.
        :type chart_id: str
        """
        self._chart_id = chart_id

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
        if not isinstance(other, DownloadChartRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
