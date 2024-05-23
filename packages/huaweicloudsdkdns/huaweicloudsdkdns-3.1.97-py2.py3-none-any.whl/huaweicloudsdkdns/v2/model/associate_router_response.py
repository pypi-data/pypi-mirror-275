# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssociateRouterResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'router_id': 'str',
        'router_region': 'str',
        'status': 'str'
    }

    attribute_map = {
        'router_id': 'router_id',
        'router_region': 'router_region',
        'status': 'status'
    }

    def __init__(self, router_id=None, router_region=None, status=None):
        """AssociateRouterResponse

        The model defined in huaweicloud sdk

        :param router_id: Router(VPC)的ID。
        :type router_id: str
        :param router_region: Router(VPC)所在的region。
        :type router_region: str
        :param status: 资源状态。
        :type status: str
        """
        
        super(AssociateRouterResponse, self).__init__()

        self._router_id = None
        self._router_region = None
        self._status = None
        self.discriminator = None

        if router_id is not None:
            self.router_id = router_id
        if router_region is not None:
            self.router_region = router_region
        if status is not None:
            self.status = status

    @property
    def router_id(self):
        """Gets the router_id of this AssociateRouterResponse.

        Router(VPC)的ID。

        :return: The router_id of this AssociateRouterResponse.
        :rtype: str
        """
        return self._router_id

    @router_id.setter
    def router_id(self, router_id):
        """Sets the router_id of this AssociateRouterResponse.

        Router(VPC)的ID。

        :param router_id: The router_id of this AssociateRouterResponse.
        :type router_id: str
        """
        self._router_id = router_id

    @property
    def router_region(self):
        """Gets the router_region of this AssociateRouterResponse.

        Router(VPC)所在的region。

        :return: The router_region of this AssociateRouterResponse.
        :rtype: str
        """
        return self._router_region

    @router_region.setter
    def router_region(self, router_region):
        """Sets the router_region of this AssociateRouterResponse.

        Router(VPC)所在的region。

        :param router_region: The router_region of this AssociateRouterResponse.
        :type router_region: str
        """
        self._router_region = router_region

    @property
    def status(self):
        """Gets the status of this AssociateRouterResponse.

        资源状态。

        :return: The status of this AssociateRouterResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AssociateRouterResponse.

        资源状态。

        :param status: The status of this AssociateRouterResponse.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, AssociateRouterResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
