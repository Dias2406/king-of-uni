"""
Provides form for creating a Team
"""
from django import forms
from group.models import Group
from account.models import Account

__author__ = "Joseph Cato"

class CreateGroupForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = ['name']


        