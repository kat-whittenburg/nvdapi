from django.shortcuts import render
from rest_framework import viewsets, mixins, filters
from rest_framework import pagination
import django_filters
from vulnerabilities.serializers import *

class VulnerabilityCursorPagination(pagination.CursorPagination):
    page_size_query_param = 'page_size'
    page_size = 25
    ordering = '-released_on'

class VulnerabilityViewSet(viewsets.GenericViewSet, mixins.ListModelMixin,
							mixins.RetrieveModelMixin):
	lookup_field = 'cve'
	paginate_by = 10
	serializer_class = VulnerabilitySerializer
	pagination_class = VulnerabilityCursorPagination

	def get_queryset(self):
		queryset = Vulnerability.objects.all()

		product = self.request.QUERY_PARAMS.get('product', None)
		if product is not None:
			queryset = queryset.filter(product_version__product__name__iexact=product)

		vendor = self.request.QUERY_PARAMS.get('vendor', None)
		if vendor is not None:
			queryset = queryset.filter(product_version__product__vendor__iexact=vendor)

		version = self.request.QUERY_PARAMS.get('version', None)
		if version is not None:
			queryset = queryset.filter(product_version__version__istartswith=version)

		return queryset