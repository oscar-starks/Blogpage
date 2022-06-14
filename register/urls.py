from django.urls import path
from . import views
from django.contrib.auth import views as auth_view


urlpatterns = [
    path('', views.myform),
    path("login/", auth_view.LoginView.as_view(template_name = "register/mylogin.html" )),
    path("logout/",auth_view.LogoutView.as_view(template_name = 'register/logout.html'))
]