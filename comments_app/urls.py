from django.urls import path

from .views import CommentListCreateView

urlpatterns = [
    path("api/comments/", CommentListCreateView.as_view(), name="comment-list-create"),
    path("comments/", CommentListCreateView.as_view(), name="comment-list-create"),
    path("", CommentListCreateView.as_view(), name="home"),
]
