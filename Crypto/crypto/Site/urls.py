from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('submit', views.submit, name='submit'),
    path('badcredentials', views.badcredentials, name='badcreds'),
    path('home', views.home, name='home'),
    path('createuser', views.createuser, name='createuser'),
    path('submitcreate', views.submitcreate, name='submitcreate'),
    path('post', views.post, name='post'),
    path('add', views.add, name='add'),
    path('remove', views.remove, name='remove'),
    path('create', views.create, name='create'),
    path('delete', views.delete, name='delete'),
    path('deletemessage/<int:messagenumber>', views.deletemessage, name='deletemessage'),
    path('messages', views.messages, name='messages'),
]