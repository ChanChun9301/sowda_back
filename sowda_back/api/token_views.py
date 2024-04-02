from rest_framework import decorators,status
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token

@decorators.api_view(['POST'])
def login_token(request):
    user =get_object_or_404(UserProd,author=request.data['author'])
    if not user.check_password(request.data['password']):
        return Response({"detail":"Not found"},status=status.HTTP_400_BAD_REQUEST)
    token = Token.objects.get_or_created(user=user)
    serializer=UserSerializer(instance=user)
    return Response({"token":token.key,"user":serializer.data})

@decorators.api_view(['POST'])
def sign_token(request):
    serializer = UserCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user=UserProd.objects.get(author=request.data['username'])
        user.set_password(request.data['password'])
        user.set_password(request.data['author'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({"token":token.key,"user":serializer.data})
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@decorators.api_view(['GET'])
@decorators.authentication_classes([SessionAuthentication,TokenAuthentication])
@decorators.permission_classes([IsAuthenticated])
def test_token(request):
    return Response({"passed for {}".format(request.user.password)})
