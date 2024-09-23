from django.contrib.auth.views import LoginView, LogoutView, PasswordResetConfirmView
from users.apps import UsersConfig
from django.urls import path
from .views import RegisterView, ProfileEditView, CustomPasswordResetView



app_name = UsersConfig.name

urlpatterns = [
    path("", LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    path("profile_edit", ProfileEditView.as_view(), name="profile_edit"),
    path("reset_password/", CustomPasswordResetView.as_view(), name="reset_password"),
    # path("password_reset_confirm/<uidb64>/<token>", PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
]
