from rest_framework import serializers

from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

    def get_children(self, obj):
        children_qs = Comment.objects.filter(parent_comment=obj)
        children_serializer = CommentSerializer(children_qs, many=True)
        return children_serializer.data
