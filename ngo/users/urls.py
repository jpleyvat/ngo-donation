from django.contrib import admin
from django.urls import path, include
from .views import (
    create_user,
    delete_user,
    UsersListView,
    UserUpdateView,
    create_profile,
    login_request
)

app_name = 'users'

urlpatterns = [
    path('createUser/', create_user, name = 'Create_User' ),
    path('<pk>/deleteUser/', delete_user.as_view(), name = 'Delete_User'),
    path('<pk>/updateUser/', UserUpdateView.as_view(), name = 'Update_User'),
    path('allusers/', UsersListView.as_view(), name='All_Users'),
    path('createProfile/', create_profile, name = 'Create_Profile' ),
    path('', include("django.contrib.auth.urls")),
    path('login/', login_request, name= 'login'),
]
