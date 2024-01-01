from django.urls import path
from .views import HomeTemplateView
from . import views

urlpatterns = [
    path('', HomeTemplateView.as_view(), name=""),
    
    path('register', views.register, name="register"),
    path('login', views.my_login, name="login"),





    
]