from . import models
from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import Http404
from django.utils import timezone
from django.views.generic import ListView,DetailView
# Create your views here.


class HomeView(ListView):
    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"


# def room_detail(request,pk):
#     try:
#         room = models.Room.objects.get(pk=pk)
#     except models.Room.DoesNotExist:
#         raise Http404()
#
#     return render(request,"rooms/detail.html",{"room":room})

"""너무나 차이가 나는 FBV와 CBV"""

class RoomDetail(DetailView):
    model = models.Room



