from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import HiddenInput

from .models import User


class UserRegisterForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"

    class Meta:
        model = User
        fields = ["email", "password1", "password2"]


class UserEditingForm(UserChangeForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password"].widget = HiddenInput()
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "phone_number", "avatar", "country" ]
