from django import forms
from group.models import Group
from account.models import Account

class CreateGroupForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = ['name']

class JoinGroupForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ['belongs_to_group']