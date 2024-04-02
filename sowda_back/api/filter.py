import django_filters
from .models import Logist

class LogistFilter(django_filters.FilterSet):
    checked = django_filters.BooleanFilter()

    class Meta:
        model = Logist
        fields = ['checked']