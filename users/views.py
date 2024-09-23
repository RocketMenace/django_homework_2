from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from config.settings import EMAIL_HOST_USER
from .forms import UserRegisterForm, UserEditingForm
from .models import User
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.hashers import make_password
from random import randint


# Create your views here.
class CustomPasswordResetView(PasswordResetView):
    success_url = reverse_lazy("catalog:product_list")


    def form_valid(self, form):
        email = form.cleaned_data["email"]
        user = User.objects.get(email=email)
        new_password = str(randint(123456, 987654))
        user.password = make_password(new_password)
        user.save()
        subject = f"Уведомление о смене пароля."
        message = f"Ваш новый пароль: {new_password}"
        send_mail(subject, message, EMAIL_HOST_USER, [email, ], fail_silently=False)
        return super().form_valid(form)


class RegisterView(CreateView):

    model = User
    form_class = UserRegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        obj = form.save()
        subject = f"Уведомление регистрации."
        message = f"Вы успешно зарегистрировались на платформе"
        send_mail(subject, message, EMAIL_HOST_USER, [obj.email,], fail_silently=False)
        return super().form_valid(form)


class ProfileEditView(UpdateView):
    model = User
    form_class = UserEditingForm
    template_name = "users/profile_edit.html"
    success_url = reverse_lazy("catalog:product_list")

    def get_object(self):
        return self.request.user
