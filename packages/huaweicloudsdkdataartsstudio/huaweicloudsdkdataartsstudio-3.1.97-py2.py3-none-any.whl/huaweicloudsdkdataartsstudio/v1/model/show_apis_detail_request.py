# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowApisDetailRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace': 'str',
        'dlm_type': 'str',
        'api_id': 'str',
        'instance_id': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'time_unit': 'str'
    }

    attribute_map = {
        'workspace': 'workspace',
        'dlm_type': 'Dlm-Type',
        'api_id': 'api_id',
        'instance_id': 'instance_id',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'time_unit': 'time_unit'
    }

    def __init__(self, workspace=None, dlm_type=None, api_id=None, instance_id=None, start_time=None, end_time=None, time_unit=None):
        """ShowApisDetailRequest

        The model defined in huaweicloud sdk

        :param workspace: 工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。
        :type workspace: str
        :param dlm_type: 数据服务的版本类型，指定SHARED共享版或EXCLUSIVE专享版。
        :type dlm_type: str
        :param api_id: api编号。
        :type api_id: str
        :param instance_id: 集群编号。
        :type instance_id: str
        :param start_time: 开始时间（13位时间戳）。
        :type start_time: int
        :param end_time: 结束时间（13位时间戳）。
        :type end_time: int
        :param time_unit: 时间单位。
        :type time_unit: str
        """
        
        

        self._workspace = None
        self._dlm_type = None
        self._api_id = None
        self._instance_id = None
        self._start_time = None
        self._end_time = None
        self._time_unit = None
        self.discriminator = None

        self.workspace = workspace
        if dlm_type is not None:
            self.dlm_type = dlm_type
        self.api_id = api_id
        if instance_id is not None:
            self.instance_id = instance_id
        self.start_time = start_time
        self.end_time = end_time
        self.time_unit = time_unit

    @property
    def workspace(self):
        """Gets the workspace of this ShowApisDetailRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :return: The workspace of this ShowApisDetailRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this ShowApisDetailRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :param workspace: The workspace of this ShowApisDetailRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def dlm_type(self):
        """Gets the dlm_type of this ShowApisDetailRequest.

        数据服务的版本类型，指定SHARED共享版或EXCLUSIVE专享版。

        :return: The dlm_type of this ShowApisDetailRequest.
        :rtype: str
        """
        return self._dlm_type

    @dlm_type.setter
    def dlm_type(self, dlm_type):
        """Sets the dlm_type of this ShowApisDetailRequest.

        数据服务的版本类型，指定SHARED共享版或EXCLUSIVE专享版。

        :param dlm_type: The dlm_type of this ShowApisDetailRequest.
        :type dlm_type: str
        """
        self._dlm_type = dlm_type

    @property
    def api_id(self):
        """Gets the api_id of this ShowApisDetailRequest.

        api编号。

        :return: The api_id of this ShowApisDetailRequest.
        :rtype: str
        """
        return self._api_id

    @api_id.setter
    def api_id(self, api_id):
        """Sets the api_id of this ShowApisDetailRequest.

        api编号。

        :param api_id: The api_id of this ShowApisDetailRequest.
        :type api_id: str
        """
        self._api_id = api_id

    @property
    def instance_id(self):
        """Gets the instance_id of this ShowApisDetailRequest.

        集群编号。

        :return: The instance_id of this ShowApisDetailRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ShowApisDetailRequest.

        集群编号。

        :param instance_id: The instance_id of this ShowApisDetailRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def start_time(self):
        """Gets the start_time of this ShowApisDetailRequest.

        开始时间（13位时间戳）。

        :return: The start_time of this ShowApisDetailRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ShowApisDetailRequest.

        开始时间（13位时间戳）。

        :param start_time: The start_time of this ShowApisDetailRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ShowApisDetailRequest.

        结束时间（13位时间戳）。

        :return: The end_time of this ShowApisDetailRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ShowApisDetailRequest.

        结束时间（13位时间戳）。

        :param end_time: The end_time of this ShowApisDetailRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def time_unit(self):
        """Gets the time_unit of this ShowApisDetailRequest.

        时间单位。

        :return: The time_unit of this ShowApisDetailRequest.
        :rtype: str
        """
        return self._time_unit

    @time_unit.setter
    def time_unit(self, time_unit):
        """Sets the time_unit of this ShowApisDetailRequest.

        时间单位。

        :param time_unit: The time_unit of this ShowApisDetailRequest.
        :type time_unit: str
        """
        self._time_unit = time_unit

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
        if not isinstance(other, ShowApisDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
