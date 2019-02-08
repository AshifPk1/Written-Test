from . models import Tenant
import django_filters

class TenantFilter(django_filters.FilterSet):
    class Meta:
        model = Tenant
        fields = ['name','age','gender','mobile_1','mobile_2','mobile_3','address_1','city','country','location',]