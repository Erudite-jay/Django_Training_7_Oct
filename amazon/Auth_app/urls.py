from django.urls import path
from .views import print_hello,home_page,user_data

urlpatterns = [
    path("hello/",print_hello),
    path("home/",home_page),
    path("get-all-data/",user_data),
]