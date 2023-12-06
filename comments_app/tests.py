import os
import tempfile

from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from .models import Comment


class CommentAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_comment_with_file(self):
        # Добавлено создание временной директории для MEDIA_ROOT
        temp_media_root = tempfile.mkdtemp()
        settings.MEDIA_ROOT = temp_media_root

        url = reverse("comments_app:comment-list-create")
        data = {
            "user_name": "TestUser",
            "email": "test@example.com",
            "text": "This is a test comment.",
            "file": SimpleUploadedFile("file.txt", b"file_content"),
        }

        response = self.client.post(url, data, format="multipart")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comment.objects.count(), 1)
        comment = Comment.objects.get()

        # Изменения начинаются здесь
        expected_file_path = os.path.normpath(os.path.join(settings.MEDIA_ROOT, comment.file.name))
        self.assertTrue(expected_file_path.endswith("comment_files/file.txt"))

    def test_get_comments(self):
        url = reverse("comments_app:comment-list-create")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
