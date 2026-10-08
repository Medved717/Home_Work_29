from django.contrib.auth.forms import UserCreationForm

from users.models import User


class UserRegister(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['email', 'password1', 'password2' ]

