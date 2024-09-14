from .models import UserBase
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserBase
        fields = ('id', 'email', 'password')