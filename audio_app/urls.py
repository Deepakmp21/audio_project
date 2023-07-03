from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("upload_file/", views.upload_file, name="upload_file"),
    path("audio_list/", views.audio_list, name="audio_list"),
    path("audio_detail/<int:audio_file_id>/", views.audio_detail, name="audio_detail"),
]
