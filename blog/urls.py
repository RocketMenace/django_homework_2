from django.urls import path
from .views import PostCreateView, PostListView, PostDetailView, PostUpdateView, PostDeleteView, PostInProcessListView, \
    make_public, republish

app_name = "blog"
urlpatterns = [
    path("posts/", PostListView.as_view(), name="posts_list"),
    path("page/<int:page>", PostListView.as_view(), name="paginator"),
    path("create_post/", PostCreateView.as_view(), name="create_post"),
    path("detail_view/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("post_edit/<int:pk>", PostUpdateView.as_view(), name="post_edit"),
    path("delete/<int:pk>/", PostDeleteView.as_view(), name="post_delete"),
    path("posts_in_process/", PostInProcessListView.as_view(), name="posts_in_process"),
    path("make_public/<int:pk>", make_public, name="make_public"),
    path("republish/<int:pk>", republish, name="republish")
]
