import django_filters
from django_filters import CharFilter

from apps.order.models import HolderType


class HolderTypeFilter(django_filters.FilterSet):
    name = CharFilter(lookup_expr='icontains')

    by_parent_id = CharFilter(method='filter_by_parent')
    get_only_parents = CharFilter(method='get_only_parents_data')

    def get_only_parents_data(self, queryset, name, value):
        return queryset.filter(parent__isnull=False)

    def filter_by_parent(self, queryset, name, value):
        return queryset.filter(parent__id=value)

    class Meta:
        model = HolderType
        fields = ['name']
