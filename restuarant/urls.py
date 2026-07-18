"""
URL configuration for restuarant project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin
admin.autodiscover()

from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import TemplateView

from menu import views


urlpatterns = [
    path(
        "accounts/login/",
        LoginView.as_view(template_name="registration/login.html"),
        name="login",
    ),
    path(
        "accounts/logout/",
        LogoutView.as_view(next_page="/"),
    ),

    path("admin/", admin.site.urls),

    path(
        "accounts/register/",
        views.register,
        name="register",
    ),

    path(
        "",
        TemplateView.as_view(template_name="index.html"),
        name="home",
    ),

    path(
        "restaurants/",
        views.RestaurantsView.as_view(),
        name="restaurant_list",
    ),
    path(
        "restaurants/new/",
        views.restaurant_create,
        name="restaurant_create",
    ),
    path(
        "restaurants/<int:pk>/",
        views.MenuView.as_view(),
        name="restaurant_detail",
    ),
    path(
        "restaurants/<int:pk>/edit/",
        views.restaurant_update,
        name="restaurant_update",
    ),
    path(
        "restaurants/<int:pk>/delete/",
        views.restaurant_delete,
        name="restaurant_delete",
    ),

    path(
        "restaurants/<int:restaurant_pk>/foods/new/",
        views.food_create,
        name="food_create",
    ),
    path(
        "foods/<int:pk>/edit/",
        views.food_update,
        name="food_update",
    ),
    path(
        "foods/<int:pk>/delete/",
        views.food_delete,
        name="food_delete",
    ),

    path(
        "restaurants/<int:pk>/comment/",
        views.CommentView.as_view(),
        name="comment_create",
    ),

    path(
        "welcome/",
        views.welcome,
        name="welcome",
    ),
]