from rest_framework.settings import api_settings
from rest_framework.viewsets import ModelViewSet

from apps.order.filters import HolderTypeFilter
from apps.order.models import HolderType, Order
from apps.order.serializers import HolderTypeSerializer, OrderSerializer


class HolderTypeViewSet(ModelViewSet):
    def get_queryset(self):
        return HolderType.objects.all()

    queryset = HolderType.objects.all()
    permission_classes = []
    serializer_class = HolderTypeSerializer
    http_method_names = ['get', ]
    filter_class = HolderTypeFilter
    renderer_classes = tuple(api_settings.DEFAULT_RENDERER_CLASSES)


class OrderModelViewSet(ModelViewSet):
    queryset = Order.objects.all()
    permission_classes = []
    serializer_class = OrderSerializer
    http_method_names = ['get', 'post', 'put', 'patch', ]
    renderer_classes = tuple(api_settings.DEFAULT_RENDERER_CLASSES)
