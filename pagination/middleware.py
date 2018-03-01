import logging

def get_page(self):
    """
    A function which will be monkeypatched onto the request to get the current
    integer representing the current page.
    """
    try:
        page = int(self.GET['page'])
        return page if page > 0 else 1
    except (KeyError, ValueError, TypeError):
        return 1


class PaginationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        request.__class__.page = property(get_page)
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
