from dataclasses import field
from django import forms
from gameKeeper.models import Building

class CreateBuildingForm(forms.ModelForm):

    class Meta:
        model = Building
        fields = ['name', 'latitude', 'longitude']