from django.urls import reverse_lazy
from django.views.generic import CreateView
from users.forms import UserRegister
from django.core.mail import send_mail
import secrets
from config.settings import EMAIL_HOST_USER
from django.shortcuts import get_object_or_404, redirect
from users.models import User
from django.urls import reverse


class RegisterView(CreateView):
    form_class = UserRegister
    template_name = 'users/register_users.html'
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        user.save()
        user.token = secrets.token_hex(16)
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email_confirm/{user.token}/'
        send_mail(
            subject='Добро пожоловать на наш сервис!',
            message=f'Для подтверждения аккаунта перейдите по следующей ссылке {url}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return super().form_valid(form)

def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse("users:login"))
