from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

from django.contrib.auth import views as auth

urlpatterns = [
    path('', views.home),
    path('profile/signup/',views.signup),
    path('profile/signup/signdata/',views.signdata),
    path('logout/',views.logout_data),
    path('licensing/',views.licensing),
    path('profile/login/',views.login_data),
    path('cartPage/',views.cartPage),
    path('profile/',views.profile),
    path('profile/addCource_form/',views.addCource_form),
    path('profile/addCource/',views.addCource),
    path('myCources/',views.myCources),
    path('addCart/',views.addCart),
    path('cartPage/addCart/',views.addCart),
    path('cource/addCart/',views.addCart),
    path('cource/<pk>/',views.showCource),
    path('cource/<pk>/addComment/',views.addComment),
    path('cource/<pk>/shippingpage/',views.shippingpage),
    path('cource/<pk>/shippingpage/shipping/',views.shipping),
]
