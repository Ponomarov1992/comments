from django.urls import path

from comments_app.views import ArticleCommentListCreateView, ArticleDetailView, ArticleListView, CommentListCreateView

app_name = "comments_app"

urlpatterns = [
    path("api/comments/", CommentListCreateView.as_view(), name="comment-list-create"),
    path("api/articles/", ArticleListView.as_view(), name="article-list"),
    path("api/articles/<int:pk>/", ArticleDetailView.as_view(), name="article-detail"),
    path(
        "api/articles/<int:article_id>/comments/", ArticleCommentListCreateView.as_view(), name="article-comment-list"
    ),
    path("", CommentListCreateView.as_view(), name="home"),
]
