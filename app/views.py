from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from .serializers import UserRegistrationSerializer, UserAuthenticationSerializer, BlogSerializer, BlogViewSerializer
from .models import Blog
from rest_framework.permissions import AllowAny, IsAuthenticated
# Create your views here.

class UserRegistrationView(APIView):
    """
    Register a new user
    """

    serializer_class = UserRegistrationSerializer
    def post(self, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserAuthenticationView(APIView):
    """
    Authentication view
    """
    serializer_class = UserAuthenticationSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            return Response({'token': user.auth_token.key}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)


class BlogPostView(APIView):
    """
    Add a blog
    """
    authentication_classes = (TokenAuthentication,)
    serializer_class = BlogSerializer
    permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogView(APIView):
    """
    See blogs
    """
    authentication_classes = (TokenAuthentication,)
    serializer_class = BlogViewSerializer
    permission_classes = (IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(Blog.objects.filter(user=request.user), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

