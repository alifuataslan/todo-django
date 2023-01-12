

from django import forms
from .models import Notes

class Listeform(forms.ModelForm):
    class Meta:
        model=Notes
        fields = ["title","content"]
