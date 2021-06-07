from django.urls import path
from . import views

#users
urlpatterns=[
    path ('', views.root),
    path ('register', views.index),
    path ('login', views.login),
    path ('new', views.new),
]