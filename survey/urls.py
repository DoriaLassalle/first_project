from django.urls import path
from . import views

#survey
urlpatterns=[
    path ('', views.index),
    path ('new', views.new),
    
]