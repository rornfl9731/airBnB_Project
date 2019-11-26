from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rooms import views as room_views

app_name = "core"

urlpatterns = [
    path('', room_views.HomeView.as_view(), name="home")
]
