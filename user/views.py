from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserBase
from .serializers import UserSerializer

class UserAPIView(APIView):
    def get(self, request):
        users = UserBase.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response({'Success': 'Cadastrado com sucesso!'}, status=status.HTTP_201_CREATED)
