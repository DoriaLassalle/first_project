from django.urls import path
from . import views

#continuacion ruta de urls de settings
urlpatterns=[
    #path ('', views.root),
    path ('', views.index),
    path ('new', views.new),
    path ('create',views.create),
    path ('<number>',views.show),
    path ('<number>/edit',views.edit),
    path ('<number>/delete',views.destroy),
    path ('json',views.bonus)
]