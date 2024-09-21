from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from .models import Post


# Create your views here.

class PostCreateView(CreateView):
    model = Post
    template_name = "post_form.html"
    fields = ["title", "content", "status", "image"]
    success_url = reverse_lazy("blog:posts_list")

    def get_context_data(self, **kwargs):
        context = super(PostCreateView, self).get_context_data()
        context["status"] = Post.Status
        return context


class PostListView(ListView):
    model = Post
    paginate_by = 2
    template_name = "posts_list.html"


class PostInProcessListView(ListView):
    model = Post
    paginate_by = 2
    template_name = "posts_in_process.html"


class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views += 1
        self.object.save()
        if self.object.views == 10:
            send_mail(subject="Django_app", message="Ваш пост достиг отметки в 10 просмотров", from_email="percivalharry@yandex.ru",
                      recipient_list=["testskyprokostin@yandex.ru"])
        return self.object


class PostUpdateView(UpdateView):
    model = Post
    template_name = "post_form.html"
    fields = ["title", "slug", "content", "status", "image"]
    success_url = reverse_lazy("blog:posts_list")


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy("blog:posts_list")
    template_name = "post_confirm_delete.html"


def make_public(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.status = "PB"
    post.save()
    return redirect(reverse_lazy("blog:posts_in_process"))


def republish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.status = "DF"
    post.save()
    return redirect(reverse_lazy("blog:posts_list"))
