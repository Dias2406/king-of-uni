"""Provides forms for Creating Building
CreateBuildingForm - form for creating new building
"""
from dataclasses import field
from django import forms
from gameKeeper.models import Building

__author__ = "Jakupov Dias"

class CreateBuildingForm(forms.ModelForm):

    class Meta:
        model = Building
        fields = ['name', 'latitude', 'longitude']