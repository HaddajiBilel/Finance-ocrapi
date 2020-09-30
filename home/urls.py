from django.urls import path
from .views import home, login

urlpatterns = [
    path('', home, name='Home'),
    path('login', login, name='register')
]
