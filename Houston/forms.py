from django import forms

class PageViewForm(forms.Form):
    path = forms.CharField(max_length=1024, required=True)
