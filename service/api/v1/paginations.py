"""
Viewset's custom paginations.
"""
from rest_framework.pagination import PageNumberPagination


class BasicPagination(PageNumberPagination):
    """
    Pagination of Providers.
    """
    page_size = 10