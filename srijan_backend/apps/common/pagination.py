from collections import OrderedDict

from django.conf import settings
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class DynamicPageSizePagination(PageNumberPagination):
    page_size_query_param = "page_size"
    max_page_size = getattr(settings, "MAX_PAGE_SIZE")
    default_page_size = getattr(settings, "DEFAULT_PAGE_SIZE")

    def get_page_size(self, request):
        if request.query_params.get(self.page_size_query_param, None):
            return int(request.query_params.get(self.page_size_query_param))
        return self.default_page_size

    def get_paginated_response(self, data):
        return Response(
            OrderedDict(
                [
                    ("num_pages", self.page.paginator.num_pages),
                    ("page", self.page.number),
                    ("count", self.page.paginator.count),
                    ("next", self.get_next_link()),
                    ("previous", self.get_previous_link()),
                    ("results", data),
                ]
            )
        )
