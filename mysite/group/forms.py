'''
Provides form for joining a Team
To also contain forms for creating and leaving a team
'''

from django import forms
from account.models import Account

__author__ = "Joseph Cato"

class JoinGroup(forms.ModelForm):

    class Meta:
        model = Account
        fields = ('belongs_to_group',) 