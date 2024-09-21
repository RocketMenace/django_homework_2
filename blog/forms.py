from .models import Post
from django.forms import ModelForm, CharField, TextInput, ImageField


class CreatePostForm(ModelForm):
    title = CharField(widget=TextInput(
        attrs={"type": "text", "class": "form-control", "id": "inputTitle", "placeholder": "Title name"}))
    content = CharField(widget=TextInput(
        attrs={"class": "form-control", "id": "exampleFormControlTextarea1", "rows": "3",
               "placeholder": "Post content"}))

    class Meta:
        model = Post
        fields = ["title", "content", "image", "status"]
