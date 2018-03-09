from django import forms
from .models import Request, Restriction


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


class RestricionForm(forms.ModelForm):
    class Meta:
        model = Restriction
        fields = ['from_date', 'to_date', 'reason']
        widgets = {
            'from_date': TextInput(),
            'to_date': TextInput()
        }


class EmailForm(forms.Form):
    email = forms.EmailField(max_length=50)
    subject = forms.CharField(widget=forms.TextInput, max_length=50)
    include_attachment = forms.BooleanField(widget=forms.CheckboxInput, initial=True, required=False)
    message = forms.CharField(widget=forms.Textarea, max_length=200)
