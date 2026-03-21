from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
User = get_user_model()
class SignupForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "email")
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'border rounded p-2',
                'placeholder': 'ユーザー名',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'border rounded p-2',
                'placeholder': 'メールアドレス',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({
            'class': 'border rounded p-2',
            'placeholder': 'パスワード',
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'border rounded p-2',
            'placeholder': 'パスワード（確認）',
        })