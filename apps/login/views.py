from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.base import View
from apps.login.models import User
from apps.login.forms import UserForm, RegisterForm


def index(request):
    pass
    return render(request, 'login/index.html')


class LoginView(View):
    def dispatch(self, request, *args, **kwargs):
        if request.session.get('is_login'):
            return redirect(reverse('login:index'))
        return super().dispatch(request, *args, **kwargs)
    def get(self, request):
        form = UserForm()
        return render(request, 'login/login.html', {
            'form': form
        })

    def post(self, request):
        form = UserForm(data=request.POST)
        message = '请填写内容！'

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(name=username)
                if user.password == password:
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    return redirect(reverse('login:index'))
                else:
                    message = '登录失败'
            except User.DoesNotExist:
                message = '用户不存在'

        return render(request, 'login/login.html', {
            'message': message,
            'form': form
        })

# def login(request):
#     if request.session.get('is_login'):
#         return redirect(reverse('login:index'))
#
#     if request.method == 'POST':
#         form = UserForm(data=request.POST)
#         message = '请填写内容！'
#
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             try:
#                 user = User.objects.get(name=username)
#                 if user.password == password:
#                     request.session['is_login'] = True
#                     request.session['user_id'] = user.id
#                     request.session['user_name'] = user.name
#                     return redirect(reverse('login:index'))
#                 else:
#                     message = '登录失败'
#             except User.DoesNotExist:
#                 message = '用户不存在'
#
#         return render(request, 'login/login.html', {
#             'message': message,
#             'form': form
#         })
#     form = UserForm()
#     return render(request, 'login/login.html', {
#         'form': form
#     })


class RegisterView(View):

    def dispatch(self, request, *args, **kwargs):
        if request.session.get('is_login'):
            return redirect(reverse('login:index'))
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = RegisterForm()
        return render(request, 'login/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        message = '请填写内容'
        if form.is_valid():
            username = form.cleaned_data['username']
            password2 = form.cleaned_data['password2']
            email = form.cleaned_data['email']
            sex = form.cleaned_data['sex']

            if User.objects.filter(name=username):
                message = '用户已经存在，请重新选择用户名！'
                return render(request, 'login/register.html', locals())

            if User.objects.filter(email=email):  # 邮箱地址唯一
                message = '该邮箱地址已被注册，请使用别的邮箱！'
                return render(request, 'login/register.html', locals())

            User.objects.create(
                name=username,
                password=password2,
                email=email,
                sex=sex
            )
            return redirect(reverse('login:login'))

# def register(request):
#     if request.session.get('is_login'):
#         return redirect(reverse('login:index'))
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         message = '请填写内容'
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password2 = form.cleaned_data['password2']
#             email = form.cleaned_data['email']
#             sex = form.cleaned_data['sex']
#
#             if User.objects.filter(name=username):
#                 message = '用户已经存在，请重新选择用户名！'
#                 return render(request, 'login/register.html', locals())
#
#             if User.objects.filter(email=email):  # 邮箱地址唯一
#                 message = '该邮箱地址已被注册，请使用别的邮箱！'
#                 return render(request, 'login/register.html', locals())
#
#             User.objects.create(
#                 name=username,
#                 password=password2,
#                 email=email,
#                 sex=sex
#             )
#             return redirect(reverse('login:login'))
#
#     form = RegisterForm()
#     return render(request, 'login/register.html', locals())


def logout(request):
    if not request.session.get('is_login'):
        return redirect(reverse('login:index'))
    request.session.flush()
    return redirect(reverse('login:index'))