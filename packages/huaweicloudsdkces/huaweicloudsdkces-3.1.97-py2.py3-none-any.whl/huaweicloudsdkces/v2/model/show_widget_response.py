# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowWidgetResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'widget_id': 'str',
        'metrics': 'list[WidgetMetric]',
        'title': 'str',
        'threshold': 'float',
        'threshold_enabled': 'bool',
        'view': 'str',
        'metric_display_mode': 'str',
        'properties': 'UpdateWidgetInfoProperties',
        'location': 'UpdateWidgetInfoLocation',
        'unit': 'str',
        'create_time': 'int'
    }

    attribute_map = {
        'widget_id': 'widget_id',
        'metrics': 'metrics',
        'title': 'title',
        'threshold': 'threshold',
        'threshold_enabled': 'threshold_enabled',
        'view': 'view',
        'metric_display_mode': 'metric_display_mode',
        'properties': 'properties',
        'location': 'location',
        'unit': 'unit',
        'create_time': 'create_time'
    }

    def __init__(self, widget_id=None, metrics=None, title=None, threshold=None, threshold_enabled=None, view=None, metric_display_mode=None, properties=None, location=None, unit=None, create_time=None):
        """ShowWidgetResponse

        The model defined in huaweicloud sdk

        :param widget_id: 视图id
        :type widget_id: str
        :param metrics: 指标列表
        :type metrics: list[:class:`huaweicloudsdkces.v2.WidgetMetric`]
        :param title: 监控视图标题
        :type title: str
        :param threshold: 监控视图指标的阈值
        :type threshold: float
        :param threshold_enabled: 阈值是否展示，true:展示，false:不展示
        :type threshold_enabled: bool
        :param view: 监控视图图表类型, bar柱状图，line折线图
        :type view: str
        :param metric_display_mode: 指标展示类型，single 单指标展示，multiple 多指标展示
        :type metric_display_mode: str
        :param properties: 
        :type properties: :class:`huaweicloudsdkces.v2.UpdateWidgetInfoProperties`
        :param location: 
        :type location: :class:`huaweicloudsdkces.v2.UpdateWidgetInfoLocation`
        :param unit: 单位
        :type unit: str
        :param create_time: 监控看板创建时间
        :type create_time: int
        """
        
        super(ShowWidgetResponse, self).__init__()

        self._widget_id = None
        self._metrics = None
        self._title = None
        self._threshold = None
        self._threshold_enabled = None
        self._view = None
        self._metric_display_mode = None
        self._properties = None
        self._location = None
        self._unit = None
        self._create_time = None
        self.discriminator = None

        if widget_id is not None:
            self.widget_id = widget_id
        if metrics is not None:
            self.metrics = metrics
        if title is not None:
            self.title = title
        if threshold is not None:
            self.threshold = threshold
        if threshold_enabled is not None:
            self.threshold_enabled = threshold_enabled
        if view is not None:
            self.view = view
        if metric_display_mode is not None:
            self.metric_display_mode = metric_display_mode
        if properties is not None:
            self.properties = properties
        if location is not None:
            self.location = location
        if unit is not None:
            self.unit = unit
        if create_time is not None:
            self.create_time = create_time

    @property
    def widget_id(self):
        """Gets the widget_id of this ShowWidgetResponse.

        视图id

        :return: The widget_id of this ShowWidgetResponse.
        :rtype: str
        """
        return self._widget_id

    @widget_id.setter
    def widget_id(self, widget_id):
        """Sets the widget_id of this ShowWidgetResponse.

        视图id

        :param widget_id: The widget_id of this ShowWidgetResponse.
        :type widget_id: str
        """
        self._widget_id = widget_id

    @property
    def metrics(self):
        """Gets the metrics of this ShowWidgetResponse.

        指标列表

        :return: The metrics of this ShowWidgetResponse.
        :rtype: list[:class:`huaweicloudsdkces.v2.WidgetMetric`]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this ShowWidgetResponse.

        指标列表

        :param metrics: The metrics of this ShowWidgetResponse.
        :type metrics: list[:class:`huaweicloudsdkces.v2.WidgetMetric`]
        """
        self._metrics = metrics

    @property
    def title(self):
        """Gets the title of this ShowWidgetResponse.

        监控视图标题

        :return: The title of this ShowWidgetResponse.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ShowWidgetResponse.

        监控视图标题

        :param title: The title of this ShowWidgetResponse.
        :type title: str
        """
        self._title = title

    @property
    def threshold(self):
        """Gets the threshold of this ShowWidgetResponse.

        监控视图指标的阈值

        :return: The threshold of this ShowWidgetResponse.
        :rtype: float
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        """Sets the threshold of this ShowWidgetResponse.

        监控视图指标的阈值

        :param threshold: The threshold of this ShowWidgetResponse.
        :type threshold: float
        """
        self._threshold = threshold

    @property
    def threshold_enabled(self):
        """Gets the threshold_enabled of this ShowWidgetResponse.

        阈值是否展示，true:展示，false:不展示

        :return: The threshold_enabled of this ShowWidgetResponse.
        :rtype: bool
        """
        return self._threshold_enabled

    @threshold_enabled.setter
    def threshold_enabled(self, threshold_enabled):
        """Sets the threshold_enabled of this ShowWidgetResponse.

        阈值是否展示，true:展示，false:不展示

        :param threshold_enabled: The threshold_enabled of this ShowWidgetResponse.
        :type threshold_enabled: bool
        """
        self._threshold_enabled = threshold_enabled

    @property
    def view(self):
        """Gets the view of this ShowWidgetResponse.

        监控视图图表类型, bar柱状图，line折线图

        :return: The view of this ShowWidgetResponse.
        :rtype: str
        """
        return self._view

    @view.setter
    def view(self, view):
        """Sets the view of this ShowWidgetResponse.

        监控视图图表类型, bar柱状图，line折线图

        :param view: The view of this ShowWidgetResponse.
        :type view: str
        """
        self._view = view

    @property
    def metric_display_mode(self):
        """Gets the metric_display_mode of this ShowWidgetResponse.

        指标展示类型，single 单指标展示，multiple 多指标展示

        :return: The metric_display_mode of this ShowWidgetResponse.
        :rtype: str
        """
        return self._metric_display_mode

    @metric_display_mode.setter
    def metric_display_mode(self, metric_display_mode):
        """Sets the metric_display_mode of this ShowWidgetResponse.

        指标展示类型，single 单指标展示，multiple 多指标展示

        :param metric_display_mode: The metric_display_mode of this ShowWidgetResponse.
        :type metric_display_mode: str
        """
        self._metric_display_mode = metric_display_mode

    @property
    def properties(self):
        """Gets the properties of this ShowWidgetResponse.

        :return: The properties of this ShowWidgetResponse.
        :rtype: :class:`huaweicloudsdkces.v2.UpdateWidgetInfoProperties`
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this ShowWidgetResponse.

        :param properties: The properties of this ShowWidgetResponse.
        :type properties: :class:`huaweicloudsdkces.v2.UpdateWidgetInfoProperties`
        """
        self._properties = properties

    @property
    def location(self):
        """Gets the location of this ShowWidgetResponse.

        :return: The location of this ShowWidgetResponse.
        :rtype: :class:`huaweicloudsdkces.v2.UpdateWidgetInfoLocation`
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this ShowWidgetResponse.

        :param location: The location of this ShowWidgetResponse.
        :type location: :class:`huaweicloudsdkces.v2.UpdateWidgetInfoLocation`
        """
        self._location = location

    @property
    def unit(self):
        """Gets the unit of this ShowWidgetResponse.

        单位

        :return: The unit of this ShowWidgetResponse.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this ShowWidgetResponse.

        单位

        :param unit: The unit of this ShowWidgetResponse.
        :type unit: str
        """
        self._unit = unit

    @property
    def create_time(self):
        """Gets the create_time of this ShowWidgetResponse.

        监控看板创建时间

        :return: The create_time of this ShowWidgetResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowWidgetResponse.

        监控看板创建时间

        :param create_time: The create_time of this ShowWidgetResponse.
        :type create_time: int
        """
        self._create_time = create_time

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
        if not isinstance(other, ShowWidgetResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
