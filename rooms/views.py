from . import models, forms
from django.shortcuts import render, redirect
from django_countries import countries
from django.core.paginator import Paginator
from django.urls import reverse
from django.http import Http404
from django.utils import timezone
from django.views.generic import ListView, DetailView, View


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


class SearchView(View):
    """ SearchView Definition """

    def get(self, request):

        country = request.GET.get("country")

        if country:

            form = forms.SearchForm(request.GET)

            if form.is_valid():

                city = form.cleaned_data.get("city")
                country = form.cleaned_data.get("country")
                room_type = form.cleaned_data.get("room_type")
                price = form.cleaned_data.get("price")
                guests = form.cleaned_data.get("guests")
                bedrooms = form.cleaned_data.get("bedrooms")
                beds = form.cleaned_data.get("beds")
                baths = form.cleaned_data.get("baths")
                instant_book = form.cleaned_data.get("instant_book")
                superhost = form.cleaned_data.get("superhost")
                amenities = form.cleaned_data.get("amenities")
                facilities = form.cleaned_data.get("facilities")

                filter_args = {}

                if city != "Anywhere":
                    filter_args["city__startswith"] = city

                filter_args["country"] = country

                if room_type is not None:
                    filter_args["room_type"] = room_type

                if price is not None:
                    filter_args["price__lte"] = price

                if guests is not None:
                    filter_args["guests__gte"] = guests

                if bedrooms is not None:
                    filter_args["bedrooms__gte"] = bedrooms

                if beds is not None:
                    filter_args["beds__gte"] = beds

                if baths is not None:
                    filter_args["baths__gte"] = baths

                if instant_book is True:
                    filter_args["instant_book"] = True

                if superhost is True:
                    filter_args["host__superhost"] = True

                for amenity in amenities:
                    filter_args["amenities"] = amenity

                for facility in facilities:
                    filter_args["facilities"] = facility

                qs = models.Room.objects.filter(**filter_args)

                paginator = Paginator(qs,10,orphans=5)

                page = request.GET.get("page",1)

                rooms = paginator.get_page(page)

                return render(request, "rooms/search.html", {"form": form, "rooms": rooms})

        else:

            form = forms.SearchForm()

        return render(request, "rooms/search.html", {"form": form})



# def search(request):
#     country = request.GET.get("country")
#
#     if country:
#         form = forms.SearchForm(request.GET)
#         if form.is_valid():
#             city = form.cleaned_data.get("city")
#             country = form.cleaned_data.get("country")
#             room_type = form.cleaned_data.get("room_type")
#             price = form.cleaned_data.get("price")
#             guests = form.cleaned_data.get("guests")
#             bedrooms = form.cleaned_data.get("bedrooms")
#             beds = form.cleaned_data.get("beds")
#             baths = form.cleaned_data.get("baths")
#             instant_book = form.cleaned_data.get("instant_book")
#             superhost = form.cleaned_data.get("superhost")
#             amenities = form.cleaned_data.get("amenities")
#             facilities = form.cleaned_data.get("facilities")
#
#             filter_args = {}
#
#             if city != "Anywhere":
#                 filter_args["city__startswith"] = city
#
#             filter_args["country"] = country
#
#             if room_type is not None:
#                 filter_args["room_type"] = room_type
#
#             if price is not None:
#                 filter_args["price__lte"] = price
#
#             if guests is not None:
#                 filter_args["guests__gte"] = guests
#
#             if bedrooms is not None:
#                 filter_args["bedrooms__gte"] = bedrooms
#
#             if beds is not None:
#                 filter_args["beds__gte"] = beds
#
#             if baths is not None:
#                 filter_args["baths__gte"] = baths
#
#             if instant_book is True:
#                 filter_args["instant_book"] = True
#
#             if superhost is True:
#                 filter_args["host__superhost"] = True
#
#             for amenity in amenities:
#                 filter_args["amenities"] = amenity
#
#             for facility in facilities:
#                 filter_args["facilities"] = facility
#
#             rooms = models.Room.objects.filter(**filter_args)
#
#     else:
#         form = forms.SearchForm()
#
#     return render(request, "rooms/search.html", {"form": form,"rooms":rooms})
