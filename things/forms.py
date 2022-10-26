"""Forms of the project."""
from django import forms

class ThingForm(forms.Form):
    name = forms.CharField(max_length=35, strip = True)
    description = forms.CharField(max_length=120, widget=forms.Textarea)
    quantity = forms.IntegerField(min_value= 0, max_value=50, widget=forms.NumberInput)
