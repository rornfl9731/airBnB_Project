from django import forms
from django_countries.fields import CountryField
from . import models

class SearchForm(forms.Form):

    city = forms.CharField(initial="Anywhere")
    country = CountryField(default="KR").formfield()
    room_type = forms.ModelChoiceField(queryset=models.RoomType.objects.all(),empty_label="Any Kind",required=False)
    price = forms.IntegerField(required=False)
    guests = forms.IntegerField(required=False)
    bedrooms = forms.IntegerField(required=False)
    beds = forms.IntegerField(required=False)
    baths = forms.IntegerField(required=False)
    instant_book = forms.BooleanField(required=False)
    superhost = forms.BooleanField(required=False)
    amenities = forms.ModelMultipleChoiceField(queryset=models.Amenity.objects.all(),widget=forms.CheckboxSelectMultiple,required=False)
    facilities = forms.ModelMultipleChoiceField(queryset=models.Facility.objects.all(),widget=forms.CheckboxSelectMultiple,required=False)
