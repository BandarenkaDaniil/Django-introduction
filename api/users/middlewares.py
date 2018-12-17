from django.utils.deprecation import MiddlewareMixin

from rest_framework.authtoken.views import Token


class CustomSessionMiddleware(MiddlewareMixin):

    def process_request(self, request, *args, **kwargs):
        try:
            token = Token.objects.get(key=request.META['HTTP_AUTHORIZATION'])
            if token:
                request.user = token.user
                print(request.user)

        except KeyError:
            pass
