from django.urls import path

from comments_app.views import CommentListCreateView


app_name = "comments_app"

urlpatterns = [
    path("comments/", CommentListCreateView.as_view(), name="comment-list-create"),
    path("api/comments/", CommentListCreateView.as_view(), name="comment-list-create"),
    path("comments/", CommentListCreateView.as_view(), name="comment-list"),
    path("", CommentListCreateView.as_view(), name="home"),
]
