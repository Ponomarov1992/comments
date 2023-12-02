from django.urls import path

from .views import CommentListCreateView
from .views import CommentListCreateAPIView


app_name = 'comments_app'

urlpatterns = [
    path("api/comments/", CommentListCreateAPIView.as_view(), name='comment-list-create'),
    path("api/comments/", CommentListCreateView.as_view(), name="comment-list-create"),
    path("comments/", CommentListCreateView.as_view(), name="comment-list-create"),
    path("", CommentListCreateView.as_view(), name="home"),
]
