from django.contrib import admin
from django.urls import path, include
from .views import create_user, delete_user, UsersListView
app_name = 'Users'

urlpatterns = [
    path('createUser/', create_user, name = 'create_user' ),
    path('deleteUser/', delete_user.as_view(), name = 'delete_user'),
    path('allusers/', UsersListView.as_view(), name='users'),


]