from django.urls import path
from .views import index, add_comment

urlpatterns = [
    path('', index, name='index'),
    path('add_comment/', add_comment, name='add_comment'),
]