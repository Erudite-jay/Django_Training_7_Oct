
from django.urls import path
from . import views

urlpatterns = [
  path("file/",views.file_upload_form),
]