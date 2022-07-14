from django.contrib import admin
from django.urls import path
from .views.main import index
from .views.signup import Signup
from .views.login import Login

urlpatterns = [
    path('', index, name='homepage'),
    path('signup', Signup.as_view()),
    path('login', Login.as_view())
]
