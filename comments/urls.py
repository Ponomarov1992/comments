from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(("comments_app.urls", "comments_app"), namespace="api")),
    path("", include("comments_app.urls")),
]
