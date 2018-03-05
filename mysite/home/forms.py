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
    email = forms.EmailField(max_length=50)
    subject = forms.CharField(widget=forms.TextInput, max_length=50)
    include_attachment = forms.BooleanField(widget=forms.CheckboxInput, initial=True, required=False)
    message = forms.CharField(widget=forms.Textarea, max_length=200)
