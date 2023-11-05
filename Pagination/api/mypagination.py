from rest_framework.pagination import PageNumberPagination


class MyPageNumberPagination(PageNumberPagination):
    page_size = 5
    page_query_param = 'p'  # for url ?page=3 instead of ?p=3 we can so
    max_page_size = 7
    