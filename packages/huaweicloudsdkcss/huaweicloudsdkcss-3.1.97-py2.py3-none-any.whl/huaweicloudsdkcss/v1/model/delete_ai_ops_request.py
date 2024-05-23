# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteAiOpsRequest:

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
        'aiops_id': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'aiops_id': 'aiops_id'
    }

    def __init__(self, cluster_id=None, aiops_id=None):
        """DeleteAiOpsRequest

        The model defined in huaweicloud sdk

        :param cluster_id: 指定待删除的集群ID。
        :type cluster_id: str
        :param aiops_id: 指定检测任务ID。
        :type aiops_id: str
        """
        
        

        self._cluster_id = None
        self._aiops_id = None
        self.discriminator = None

        self.cluster_id = cluster_id
        self.aiops_id = aiops_id

    @property
    def cluster_id(self):
        """Gets the cluster_id of this DeleteAiOpsRequest.

        指定待删除的集群ID。

        :return: The cluster_id of this DeleteAiOpsRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this DeleteAiOpsRequest.

        指定待删除的集群ID。

        :param cluster_id: The cluster_id of this DeleteAiOpsRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def aiops_id(self):
        """Gets the aiops_id of this DeleteAiOpsRequest.

        指定检测任务ID。

        :return: The aiops_id of this DeleteAiOpsRequest.
        :rtype: str
        """
        return self._aiops_id

    @aiops_id.setter
    def aiops_id(self, aiops_id):
        """Sets the aiops_id of this DeleteAiOpsRequest.

        指定检测任务ID。

        :param aiops_id: The aiops_id of this DeleteAiOpsRequest.
        :type aiops_id: str
        """
        self._aiops_id = aiops_id

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
        if not isinstance(other, DeleteAiOpsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
