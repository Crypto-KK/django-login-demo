from django.urls import reverse
from django.shortcuts import redirect


class RedirectMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(request)
        # if request.session.get('is_login'):
        #     return redirect(reverse('login:index'))
        response = self.get_response
        return response