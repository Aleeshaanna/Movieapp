from django import forms
from app.models import Movie



class movieform(forms.ModelForm): #form defenition
    class Meta:
        model=Movie
        fields='__all__'
