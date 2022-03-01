from django import forms
from territoryGame.models import TerritoryCapture
from account.models import Account

class CreateTerritoryCaptureForm(forms.ModelForm):

    class Meta:
        model = TerritoryCapture
        fields = ['comment']

class UserLocationForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ['latitude', 'longitude']