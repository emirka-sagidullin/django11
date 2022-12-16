from django import forms

class Section(forms.Form):
    Heading = forms.CharField()
    URL = forms.URLField()
    Content = forms.CharField(widget=forms.Textarea)
    Publication = forms.CharField(widget=forms.CheckboxInput)
