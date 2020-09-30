from django.urls import path
from .views import home

urlpatterns = [
    path('home/', home, name='Home'),
    #path('', signin, name='register')
]
