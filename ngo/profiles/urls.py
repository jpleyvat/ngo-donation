'''Profiles urls.'''

# Django.
from django.urls import path

# Views.
from . import views

app_name = 'profile'

urlpatterns = [
    path('<int:pk>/', views.ProfileUpdate.as_view(), name = 'update'),
    # path('<pk>/update/', ProfileUpdate.as_view(), name = 'update'),
]

