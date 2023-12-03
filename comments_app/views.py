from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response

from .models import Article, ArticleComment, Comment
from .serializers import ArticleCommentSerializer, ArticleSerializer, CommentSerializer


class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    ordering_fields = ["created_at"]
    ordering = ["-created_at"]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["parent"] = self.request.query_params.get("parent", None)
        return context

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ArticleListView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    ordering_fields = ["created_at"]
    ordering = ["-created_at"]


class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleCommentListCreateView(generics.ListCreateAPIView):
    serializer_class = ArticleCommentSerializer
    ordering_fields = ["created_at"]
    ordering = ["-created_at"]

    def get_queryset(self):
        article_id = self.kwargs["article_id"]
        return ArticleComment.objects.filter(article_id=article_id)

    def perform_create(self, serializer):
        article_id = self.kwargs["article_id"]
        article = get_object_or_404(Article, pk=article_id)
        serializer.save(article=article)
