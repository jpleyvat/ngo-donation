from django.contrib import admin
from django.urls import path, include
from .views import create_user, delete_user, UsersListView
app_name = 'users'

urlpatterns = [
    path('createUser/', create_user, name = 'Create_User' ),
    path('<pk>/deleteUser/', delete_user.as_view(), name = 'Delete_User'),
    path('allusers/', UsersListView.as_view(), name='All_Users'),


]