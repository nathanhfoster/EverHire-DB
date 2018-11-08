from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.conf import settings
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from django.contrib.auth.models import update_last_login


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        update_last_login(None, user)   
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'token': token.key,
            'id': user.pk,
            'profile_image': user.profile_image,
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'is_active': user.is_active,
            'last_login': user.last_login,
        })

        

# class TokenAuthenticationView(ObtainAuthToken):
#     """Implementation of ObtainAuthToken with last_login update"""

#     def post(self, request):
#         result = super(TokenAuthenticationView, self).post(request)
#         try:
#             request_user, data = requests.get_parameters(request)
#             user = requests.get_user_by_username(data['username'])
#             update_last_login(None, user)            
#         except Exception as exc:
#             return None
#         return result