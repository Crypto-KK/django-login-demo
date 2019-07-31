from captcha.fields import CaptchaField
from django import forms

from apps.login.models import User


class UserForm(forms.Form):
    username = forms.CharField(label='用户', max_length=128,
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control'}
                               ))
    password = forms.CharField(label='密码', max_length=256,
                               widget=forms.PasswordInput(
                                   attrs={'class': 'form-control'}
                               ))

    captcha = CaptchaField(label='验证码')


class RegisterForm(forms.Form):
    gender = (
        ('male', '男'),
        ('female', '女')
    )
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="确认密码", max_length=256,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="邮箱地址", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    sex = forms.ChoiceField(label='性别', choices=gender)
    captcha = CaptchaField(label='验证码')

    def clean(self):
        cleaned_data = self.cleaned_data
        password1 = cleaned_data['password1']
        password2 = cleaned_data['password2']
        if password1 != password2:
            raise forms.ValidationError('输入密码不匹配')

        return cleaned_data