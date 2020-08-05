from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('', include("basicinfo.urls")),
    path('basicinfo/', include("basicinfo.urls")),
]
