# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCatalogListResponse(SdkResponse):

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
        'catalogs': 'list[RecordForGetAllCatalog]'
    }

    attribute_map = {
        'total': 'total',
        'catalogs': 'catalogs'
    }

    def __init__(self, total=None, catalogs=None):
        """ListCatalogListResponse

        The model defined in huaweicloud sdk

        :param total: 符合条件的数据总数
        :type total: int
        :param catalogs: 本次返回的APP列表
        :type catalogs: list[:class:`huaweicloudsdkdataartsstudio.v1.RecordForGetAllCatalog`]
        """
        
        super(ListCatalogListResponse, self).__init__()

        self._total = None
        self._catalogs = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if catalogs is not None:
            self.catalogs = catalogs

    @property
    def total(self):
        """Gets the total of this ListCatalogListResponse.

        符合条件的数据总数

        :return: The total of this ListCatalogListResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListCatalogListResponse.

        符合条件的数据总数

        :param total: The total of this ListCatalogListResponse.
        :type total: int
        """
        self._total = total

    @property
    def catalogs(self):
        """Gets the catalogs of this ListCatalogListResponse.

        本次返回的APP列表

        :return: The catalogs of this ListCatalogListResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.RecordForGetAllCatalog`]
        """
        return self._catalogs

    @catalogs.setter
    def catalogs(self, catalogs):
        """Sets the catalogs of this ListCatalogListResponse.

        本次返回的APP列表

        :param catalogs: The catalogs of this ListCatalogListResponse.
        :type catalogs: list[:class:`huaweicloudsdkdataartsstudio.v1.RecordForGetAllCatalog`]
        """
        self._catalogs = catalogs

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
        if not isinstance(other, ListCatalogListResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
