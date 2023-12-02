from django.shortcuts import redirect, render

from .forms import CommentForm
from .models import Comment


def index(request):
    comments = Comment.objects.filter(parent_comment__isnull=True).order_by("-created_at")
    return render(request, "comments_app/index.html", {"comments": comments})


def add_comment(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = CommentForm()
    return render(request, "comments_app/add_comment.html", {"form": form})
