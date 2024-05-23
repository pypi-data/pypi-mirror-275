# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchShowEdgeAppVersionsRequest:

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
        'edge_app_id': 'str',
        'version': 'str',
        'offset': 'int',
        'limit': 'int',
        'state': 'str'
    }

    attribute_map = {
        'instance_id': 'Instance-Id',
        'edge_app_id': 'edge_app_id',
        'version': 'version',
        'offset': 'offset',
        'limit': 'limit',
        'state': 'state'
    }

    def __init__(self, instance_id=None, edge_app_id=None, version=None, offset=None, limit=None, state=None):
        """BatchShowEdgeAppVersionsRequest

        The model defined in huaweicloud sdk

        :param instance_id: **参数说明**：实例ID。dris物理实例的唯一标识。获取方法参见[获取Instance-Id](https://support.huaweicloud.com/api-v2x/v2x_04_0030.html)。  **取值范围**：仅支持数字，小写字母和连接符（-）的组合，长度36。
        :type instance_id: str
        :param edge_app_id: **参数说明**：用户自定义应用唯一ID。  **取值范围**：只允许字母、数字、下划线（_）、连接符（-）、美元符号（$）的组合。
        :type edge_app_id: str
        :param version: **参数说明**：应用版本搜索关键字。
        :type version: str
        :param offset: **参数说明**：分页查询时的页码。
        :type offset: int
        :param limit: **参数说明**：每页记录数。
        :type limit: int
        :param state: **参数说明**：应用版本状态。  **取值范围**：  - DRAFT：草稿  - PUBLISHED：发布  - OFF_SHELF：下线
        :type state: str
        """
        
        

        self._instance_id = None
        self._edge_app_id = None
        self._version = None
        self._offset = None
        self._limit = None
        self._state = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        self.edge_app_id = edge_app_id
        if version is not None:
            self.version = version
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if state is not None:
            self.state = state

    @property
    def instance_id(self):
        """Gets the instance_id of this BatchShowEdgeAppVersionsRequest.

        **参数说明**：实例ID。dris物理实例的唯一标识。获取方法参见[获取Instance-Id](https://support.huaweicloud.com/api-v2x/v2x_04_0030.html)。  **取值范围**：仅支持数字，小写字母和连接符（-）的组合，长度36。

        :return: The instance_id of this BatchShowEdgeAppVersionsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this BatchShowEdgeAppVersionsRequest.

        **参数说明**：实例ID。dris物理实例的唯一标识。获取方法参见[获取Instance-Id](https://support.huaweicloud.com/api-v2x/v2x_04_0030.html)。  **取值范围**：仅支持数字，小写字母和连接符（-）的组合，长度36。

        :param instance_id: The instance_id of this BatchShowEdgeAppVersionsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def edge_app_id(self):
        """Gets the edge_app_id of this BatchShowEdgeAppVersionsRequest.

        **参数说明**：用户自定义应用唯一ID。  **取值范围**：只允许字母、数字、下划线（_）、连接符（-）、美元符号（$）的组合。

        :return: The edge_app_id of this BatchShowEdgeAppVersionsRequest.
        :rtype: str
        """
        return self._edge_app_id

    @edge_app_id.setter
    def edge_app_id(self, edge_app_id):
        """Sets the edge_app_id of this BatchShowEdgeAppVersionsRequest.

        **参数说明**：用户自定义应用唯一ID。  **取值范围**：只允许字母、数字、下划线（_）、连接符（-）、美元符号（$）的组合。

        :param edge_app_id: The edge_app_id of this BatchShowEdgeAppVersionsRequest.
        :type edge_app_id: str
        """
        self._edge_app_id = edge_app_id

    @property
    def version(self):
        """Gets the version of this BatchShowEdgeAppVersionsRequest.

        **参数说明**：应用版本搜索关键字。

        :return: The version of this BatchShowEdgeAppVersionsRequest.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this BatchShowEdgeAppVersionsRequest.

        **参数说明**：应用版本搜索关键字。

        :param version: The version of this BatchShowEdgeAppVersionsRequest.
        :type version: str
        """
        self._version = version

    @property
    def offset(self):
        """Gets the offset of this BatchShowEdgeAppVersionsRequest.

        **参数说明**：分页查询时的页码。

        :return: The offset of this BatchShowEdgeAppVersionsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this BatchShowEdgeAppVersionsRequest.

        **参数说明**：分页查询时的页码。

        :param offset: The offset of this BatchShowEdgeAppVersionsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this BatchShowEdgeAppVersionsRequest.

        **参数说明**：每页记录数。

        :return: The limit of this BatchShowEdgeAppVersionsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this BatchShowEdgeAppVersionsRequest.

        **参数说明**：每页记录数。

        :param limit: The limit of this BatchShowEdgeAppVersionsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def state(self):
        """Gets the state of this BatchShowEdgeAppVersionsRequest.

        **参数说明**：应用版本状态。  **取值范围**：  - DRAFT：草稿  - PUBLISHED：发布  - OFF_SHELF：下线

        :return: The state of this BatchShowEdgeAppVersionsRequest.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this BatchShowEdgeAppVersionsRequest.

        **参数说明**：应用版本状态。  **取值范围**：  - DRAFT：草稿  - PUBLISHED：发布  - OFF_SHELF：下线

        :param state: The state of this BatchShowEdgeAppVersionsRequest.
        :type state: str
        """
        self._state = state

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
        if not isinstance(other, BatchShowEdgeAppVersionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
