
from django.shortcuts import redirect
from django.urls import reverse


class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == '/login/' and request.user.is_authenticated:
            return redirect(reverse('home:index'))
        elif request.path == '/' or request.path == '':
            response = self.get_response(request)
        elif not request.user.is_authenticated and request.path != reverse('login'):
            return redirect(reverse('login') + '?next=' + request.path)
        else:
            response = self.get_response(request)
        return response
