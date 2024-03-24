import secrets
import random

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView, UpdateView

from users.forms import RegistrationForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = RegistrationForm

    def get_success_url(self):
        return reverse("users:login")

    def form_valid(self, form):
        user = form.save()
        token = secrets.token_hex(16)
        user.token = token
        user.is_active = False
        user.save()
        host = self.request.get_host()
        url = f"http://{host}/users/verify/{token}/"
        message = f"Добрый день! Для завершения регистрации, подтвердите адрес электронной почты: {url}"
        send_mail(
            "Подтвердите адрес электронной почты",
            message,
            settings.EMAIL_HOST_USER,
            [
                user.email,
            ],
        )
        return super().form_valid(form)


def verify(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse("users:login"))


def reset_password(request):
    new_password = ''.join([str(random.randint(0, 9)) for _ in range(8)])
    send_mail(
        subject='Вы сменили пароль',
        message=f'Ваш новый пароль : {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]
    )
    request.user.set_password(new_password)
    request.user.save()
    return redirect(reverse('users:login'))