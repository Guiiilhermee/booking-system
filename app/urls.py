from django.urls import path
from .views import HomeTemplateView
from . import views

urlpatterns = [
    path('', HomeTemplateView.as_view(), name="home"),
    
    path('register', views.register, name="register"),
    
    path('login', views.my_login, name="login"),
    
    path('logout', views.user_logout, name="logout"),

    
    
# CRUD
    
    path('dashboard', views.dashboard, name="dashboard"),
    
    path('create-record', views.create_record, name="create-record"),

    
    






    
]