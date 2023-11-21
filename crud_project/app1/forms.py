from .models import Data
from django import forms
class Data_forms(forms.ModelForm):
  class Meta:
    Model=Data
    fields='__all__'
    