from django.urls import path
from django.contrib import admin
from . import views
urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),

]
