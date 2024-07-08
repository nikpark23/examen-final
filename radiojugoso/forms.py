from django import forms
from django.contrib.auth.forms import UserCreationForm ,UserChangeForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
        
        #cambio de contraseña en editar


class CustomUserChangeForm(UserChangeForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput, required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password', 'is_active', 'is_staff')

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password')
        if password:
            user.set_password(password)
        if commit:
            user.save()
        return user