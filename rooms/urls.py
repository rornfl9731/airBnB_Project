from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "rooms"

urlpatterns = [
    # path('<int:pk>', views.room_detail, name="detail")
    path('<int:pk>',views.RoomDetail.as_view(),name="detail")
]
