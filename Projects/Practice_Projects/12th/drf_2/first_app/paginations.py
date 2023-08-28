from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

class ProductPagination(PageNumberPagination):
    page_size = 3
    
    #OPTIONALS:
    page_query_param = 'p' # search box e page er sthan e p lekha ashbe.
    page_size_query_param = 'size'
    max_page_size = 100
    
class ProductLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 4
    limit_query_param = 'l'
    offset_query_param = 'start'
    max_limit = 3
    
class ProductCursorPagination(CursorPagination):
    page_size = 3
    ordering = 'price'
    cursor_query_param = 'data'