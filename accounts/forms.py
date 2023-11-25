from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomerUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomerUser
        fields = ('username', 'birth_day', 'email')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomerUser
        fields = ('username', 'birth_day', 'email')