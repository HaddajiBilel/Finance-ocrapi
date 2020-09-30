from django.urls import path
from .views import home, signin

urlpatterns = [
    path('', home, name='Home'),
    path('login', signin, name='register')
]
