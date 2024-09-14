from django.urls import path
from .views import UserAPIView, UsersAPIView

urlpatterns = [
    path('<int:user_id>/', UserAPIView.as_view(), name='user'),
    path('users/', UsersAPIView.as_view(), name='users'),
]