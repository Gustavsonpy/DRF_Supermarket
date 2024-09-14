from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserBase
from .serializers import UserSerializer

class UsersAPIView(APIView):
    def get(self, request):
        users = UserBase.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data = request.data)
        print(f'\n\nrequest: {request}\n\n')
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response({'Success': 'Cadastrado com sucesso!'}, status=status.HTTP_201_CREATED)

class UserAPIView(APIView):
    def get(self, request, user_id):
        users = UserBase.objects.get(id=user_id)
        serializer = UserSerializer(users)
        return Response(serializer.data)
    
    def put(self, request, user_id):
        user = UserBase.objects.get(id = user_id)
        serializer = UserSerializer(user, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Updated': 'The user has been updated!'})
        return Response({'Error': 'Error to update the user'})
    
    def delete(self, request, user_id): #It's necessary put the 'request' in paramaters for DRF knows the method you want
        user = UserBase.objects.get(id = user_id)
        user.delete()
        return Response({'success': 'User deleted successfully'})