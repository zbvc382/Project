from django import forms
from home.models import Requests


class DateInput(forms.DateInput):
    input_type = 'date'


class RequestForm(forms.ModelForm):

    class Meta:
        model = Requests
        fields = ['leave_type', 'start', 'end', 'reason']
        widgets = {
            'start': DateInput(),
            'end': DateInput()
        }
