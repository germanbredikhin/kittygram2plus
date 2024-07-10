from rest_framework.pagination import Response
from rest_framework.pagination import BasePagination, PageNumberPagination


class CustomPagination(PageNumberPagination):
    page_size = 10

    def get_paginated_response(self, data):
        return Response({
#            'links': {
#                'next page': self.get_next_link(),
#                'previous page': self.get_previous_link()
#            },
            'cats count': self.page.paginator.count,
            'response': data
        })
