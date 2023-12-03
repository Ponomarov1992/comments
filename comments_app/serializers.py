from rest_framework import serializers

from .models import Article, ArticleComment, Comment


class CommentSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = "__all__"
        extra_kwargs = {
            "file": {"required": False, "allow_empty_file": True},
            "image": {"required": False, "allow_empty_file": True},
        }

    def get_children(self, obj):
        children_qs = Comment.objects.filter(parent_comment=obj)
        children_serializer = CommentSerializer(children_qs, many=True)
        return children_serializer.data


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"


class ArticleCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleComment
        fields = "__all__"
