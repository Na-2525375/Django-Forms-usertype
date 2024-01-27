from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name='home'),
    path('', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('create_person/', views.create_person, name='create_person'),
]