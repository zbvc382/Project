from django import forms
from .models import Request


class DateInput(forms.DateInput):
    input_type = 'date'


class TextInput(forms.TextInput):
    input_type = 'text'


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['leave_type', 'start', 'end', 'reason', 'attachment']
        widgets = {
            'start': TextInput(),
            'end': TextInput()
        }


class EmailForm(forms.Form):
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
