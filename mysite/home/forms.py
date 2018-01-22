from django import forms
from .models import Requests


class DateInput(forms.DateInput):
    input_type = 'date'


class RequestForm(forms.ModelForm):
    class Meta:
        model = Requests
        fields = ['leave_type', 'start', 'end', 'reason', 'attachment']
        widgets = {
            'start': DateInput(),
            'end': DateInput()
        }