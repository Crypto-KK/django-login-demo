from django.urls import path
from apps.login import views

app_name = 'login'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.logout, name='logout'),
]