from django.urls import path
from .views import FileView, TableView

urlpatterns = [
    path('', FileView.as_view()),
    path('api/<slug:fileID>/', TableView.as_view())
]
