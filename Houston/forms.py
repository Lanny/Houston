from django import forms

class PageViewForm(forms.Form):
    path = forms.CharField(max_length=1024, required=True)

GRANULARITY_CHOICES = (
    ('month', 'by month'),
    ('day', 'by day'),
    ('hour', 'by hour'),
    ('minute', 'by minute'))

class ViewCountsForm(forms.Form):
    start_time = forms.DateTimeField(required=True)
    end_time = forms.DateTimeField(required=True)
    granularity = forms.ChoiceField(required=True, choices=GRANULARITY_CHOICES)
