from django import forms
from home.models import Requests


class RequestForm(forms.ModelForm):

    class Meta:
        model = Requests
        fields = ['leave_type', 'start', 'end', 'reason']
