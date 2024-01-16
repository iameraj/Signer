from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login_me, name="login"),
    path("logout/", views.logut, name="logout"),
]
