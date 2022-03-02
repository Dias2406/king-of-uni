"""Provides forms for Capturing the territory
CreateTerritoryCaptureForm - form for creating new territory capture
UserLocationForm - form for saving user location
"""
from django import forms
from territoryGame.models import TerritoryCapture
from account.models import Account

__author__ = "Jakupov Dias"

class CreateTerritoryCaptureForm(forms.ModelForm):

    class Meta:
        model = TerritoryCapture
        fields = ['comment']

class UserLocationForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ['latitude', 'longitude']