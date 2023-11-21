from django import forms
from reg.models import Empreg
class RegForm(forms.ModelForm):
  # name=forms.CharField()
  # email=forms.EmailField()
  class Meta:
    model=Empreg
    fields='__all__'