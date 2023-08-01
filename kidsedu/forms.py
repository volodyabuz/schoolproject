from django import forms
from .models import *
import re
from django.core.exceptions import ValidationError

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
                'placeholder': "Ivanivanov@gmail.com"
            }),
            'phone_number': forms.TextInput(attrs={
                "type": "tel",
                'class': "form-control",
                'name': "cf-phone",
                'placeholder': "+1-234-567-89-01",
                'pattern': "+7-[0-9]{3}-[0-9]{3}-[0-9]{2}-[0-9]{2}",
                'required': None,
            }),
            'add_text': forms.Textarea(attrs={
                'class': "form-control",
                'rows': "3",
                'name': "cf-message",
                'placeholder': "Дополнительное сообщение"
            }),
        }

    def clean_phone_number(self):
        """Проверяет корректность формата номера телефона."""
        phone_number = self.cleaned_data['phone_number']
        match = re.findall(r'\+7-[0-9]{3}-[0-9]{3}-[0-9]{2}-[0-9]{2}', phone_number)
        if phone_number != ''.join(match):
            raise ValidationError('Введенный номер не соответствует формату')

        return phone_number
