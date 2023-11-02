from django import forms
from .models import *
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField


class AddPersonForm(forms.ModelForm):
    """Форма добавления пользователя."""

    class Meta:
        model = PersonForm
        fields = ['person', 'email', 'phone_number', 'add_text']
        widgets = {
            'person': forms.TextInput(attrs={
                'type': "text",
                'class': "form-control",
                'name': "cf-name",
                'placeholder': "Иван Иванов"
            }),
            'email': forms.EmailInput(attrs={
                'type': "email",
                'class': "form-control",
                'name': "cf-email",
                'placeholder': "Ivanivanov@gmail.com",
                'required pattern': "[a-z0-9]+@[a-z]+\.[a-z]{2,3}"
            }),
            'phone_number': forms.TextInput(attrs={
                "type": "tel",
                'class': "form-control",
                'name': "cf-phone",
                'placeholder': "+1-234-567-89-01",
                'required pattern': "\+7-[0-9]{3}-[0-9]{3}-[0-9]{2}-[0-9]{2}",
            }),
            'add_text': forms.Textarea(attrs={
                'class': "form-control",
                'rows': "3",
                'name': "cf-message",
                'placeholder': "Дополнительное сообщение"
            }),
        }

    # def clean_phone_number(self):
    #     """Проверяет корректность формата номера телефона."""
    #     phone_number = self.cleaned_data['phone_number']
    #     match = re.findall(r'\+7-[0-9]{3}-[0-9]{3}-[0-9]{2}-[0-9]{2}', phone_number)
    #     if phone_number != ''.join(match):
    #         raise ValidationError('Введенный номер не соответствует формату', code='invalid')

    #     return phone_number


class FeedBackForm(forms.Form):
    """Форма обратной связи."""

    name = forms.CharField(max_length=40, widget=forms.TextInput(attrs={
        'type': "text",
        'class': "form-control",
        'name': "cf-name",
        'placeholder': "Имя",
        'required': "required"
    })
    )
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'type': "email",
        'class': "form-control",
        'name': "cf-email",
        'placeholder': "Email",
        'required pattern': "[a-z0-9]+@[a-z]+\.[a-z]{2,3}",
        'required': "required"
        })
    )
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': "form-control",
        'rows': "7",
        'name': "cf-message",
        'placeholder': "Сообщение",
    })
    )
    captcha = CaptchaField()


class RegisterForm(UserCreationForm):
    """Форма регистрации пользователей."""

    username = forms.CharField(max_length=40, widget=forms.TextInput(attrs={
        'type': "text",
        'class': "form-control",
        'name': "cf-name",
        'placeholder': "Имя пользователя",
        'required': "required"
    })
    )
    password1 = forms.CharField(max_length=40, widget=forms.PasswordInput(attrs={
        'class': "form-control",
        'name': "cf-password",
        'placeholder': "Пароль",
        'required': "required"
    })
    )
    password2 = forms.CharField(max_length=40, widget=forms.PasswordInput(attrs={
        'class': "form-control",
        'name': "cf-password",
        'placeholder': "Подтверждение пароля",
        'required': "required"
    })
    )

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
