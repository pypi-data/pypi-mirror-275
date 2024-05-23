# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAgentsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_id': 'str',
        'namespace': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'namespace': 'namespace'
    }

    def __init__(self, cluster_id=None, namespace=None):
        """ListAgentsRequest

        The model defined in huaweicloud sdk

        :param cluster_id: - 查询集群主机时，填写集群id。 - 查询用户自定义主机时，填写“apm”。
        :type cluster_id: str
        :param namespace: - 查询集群主机时，填写命名空间。 - 查询用户自定义主机时，填写“apm”。
        :type namespace: str
        """
        
        

        self._cluster_id = None
        self._namespace = None
        self.discriminator = None

        self.cluster_id = cluster_id
        self.namespace = namespace

    @property
    def cluster_id(self):
        """Gets the cluster_id of this ListAgentsRequest.

        - 查询集群主机时，填写集群id。 - 查询用户自定义主机时，填写“apm”。

        :return: The cluster_id of this ListAgentsRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this ListAgentsRequest.

        - 查询集群主机时，填写集群id。 - 查询用户自定义主机时，填写“apm”。

        :param cluster_id: The cluster_id of this ListAgentsRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def namespace(self):
        """Gets the namespace of this ListAgentsRequest.

        - 查询集群主机时，填写命名空间。 - 查询用户自定义主机时，填写“apm”。

        :return: The namespace of this ListAgentsRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this ListAgentsRequest.

        - 查询集群主机时，填写命名空间。 - 查询用户自定义主机时，填写“apm”。

        :param namespace: The namespace of this ListAgentsRequest.
        :type namespace: str
        """
        self._namespace = namespace

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
        if not isinstance(other, ListAgentsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
