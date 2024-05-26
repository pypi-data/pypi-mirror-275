from collections import OrderedDict

from django.core.paginator import InvalidPage
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.utils.urls import replace_query_param


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000
    page = None
    request = None

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('page_size', self.page.paginator.per_page),
            ('page_number', self.page.number),
            ('next_page_number', self.page.next_page_number() if self.page.has_next() else None),
            ('previous_page_number', self.page.previous_page_number() if self.page.has_previous() else None),
            ('next_page_link', self.get_next_link()),
            ('previous_page_link', self.get_previous_link()),
            ('results', data)
        ]))

    def get_previous_link(self):
        if not self.page.has_previous():
            return None
        url = self.request.build_absolute_uri()
        page_number = self.page.previous_page_number()
        return replace_query_param(url, self.page_query_param, page_number)

    def paginate_queryset(self, queryset, request, view=None):
        page_size = self.get_page_size(request)
        if not page_size:
            return None
        paginator = self.django_paginator_class(queryset, page_size)
        page_number = self.get_page_number(request, paginator)
        try:
            page_number = int(page_number)
            if page_number < 1:
                page_number = 1
            self.page = paginator.page(page_number)
        except ValueError:
            self.page = paginator.page(1)
        except TypeError:
            self.page = paginator.page(1)
        except InvalidPage:
            self.page = paginator.page(self.get_last_page_number(queryset, page_size))

        if paginator.num_pages > 1 and self.template is not None:
            # The browsable API should display pagination controls.
            self.display_page_controls = True

        self.request = request
        return list(self.page)

    def get_last_page_number(self, queryset, page_size=1):
        total_items = queryset.count()  # Assuming queryset is the entire set of items
        last_page_number = (total_items + page_size - 1) // page_size
        return last_page_number
