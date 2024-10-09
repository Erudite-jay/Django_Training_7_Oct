from django.urls import path
from .views import print_hello,home_page,user_data,single_user_data

urlpatterns = [
    path("hello/",print_hello),
    path("home/",home_page),
    path("get-all-data/",user_data),
    path("single-user-data/<str:pk>/",single_user_data),
    
]