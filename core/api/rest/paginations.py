from rest_framework.pagination import PageNumberPagination


class BasePageNumberPagination(PageNumberPagination):
    page_size_query_param = 'sizePerPage'
    page_size = 10
