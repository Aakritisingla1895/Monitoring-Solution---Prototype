from unicodedata import name
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('',views.userlogin),
    path('signup',views.signup,name='signup'),
    path('home',views.home,name='home'),
    path('notifications', views.notifications,name='notifications'),
    path('charts', views.charts, name='charts'),
    path('orders', views.orders, name='orders'),
]