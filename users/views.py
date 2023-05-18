from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from users.models import Confirm_User
from users.serializers import UserCreateSerializer, UserAuthorizeSerializer, ConfirmUserSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


class AuthorizationAPIView(APIView):
    def post(self, request):
        serializer = UserAuthorizeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(**serializer.validated_data)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response(data={'key': token.key})
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class RegistrationAPIView(APIView):
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')
        user = User.objects.create(username=username, password=password, is_active=False)
        confirm_user = Confirm_User(user=user)
        confirm_user.code = confirm_user.generate_random_code()
        confirm_user.save()

        return Response(data={'user_id': user.id})


class ConfirmUserAPIView(APIView):
    def post(self, request):
        serializer = ConfirmUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            confirm_user = Confirm_User.objects.get(code=request.data['code'])
            user = confirm_user.user
            user.is_active = True
            user.save()
            return Response(status=status.HTTP_200_OK, data={'Ok!': 'User is active'})
        except Confirm_User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'error': 'Code or id not found!'})

# @api_view(['POST'])
# def registration_api_view(request):
#     serializer = UserCreateSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     username = request.data.get('username')
#     password = request.data.get('password')
#     user = User.objects.create_user(username=username, password=password)
#     return Response(data={'user_id': user.id})


# @api_view(['POST'])
# def authorization_api_view(request):
#     """ Validate Data """
#     serializer = UserAuthorizeSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     """ Authenticate (Search) User """
#     user = authenticate(**serializer.validated_data)
#     if user:
#         """ Authorize User """
#         # Token.objects.filter(user=user).delete()
#         # token = Token.objects.create(user=user)
#         token, created = Token.objects.get_or_create(user=user)
#         return Response(data={'key': token.key})
#     """ Error on Unauthorized """
#     return Response(status=status.HTTP_401_UNAUTHORIZED)
