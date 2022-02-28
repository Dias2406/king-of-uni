from django import forms
from account.models import Account

class JoinGroup(forms.ModelForm):

    class Meta:
        model = Account
        fields = ('belongs_to_group',) 