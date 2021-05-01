import django_filters
from django_filters import DateFilter , CharFilter
from .models import *


class efilter(django_filters.FilterSet):
	name = CharFilter(field_name='name' , lookup_expr='icontains' , label='Name')
	phone = CharFilter(field_name='phone' , lookup_expr='icontains' , label='Phone')
	address = CharFilter(field_name='address' , lookup_expr='icontains' , label='Address')
	class Meta:
		model=employee
		fields = [ 'name' , 'position' , 'dept' , 'phone' , 'address']


