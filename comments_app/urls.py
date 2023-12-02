from django.urls import path

from .views import add_comment, index

urlpatterns = [
    path("", index, name="index"),
    path("add_comment/", add_comment, name="add_comment"),
]
