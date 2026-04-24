from django import forms
from core.models import Resume
from .models import Section

#-----------PORTFOLIO FORM------------------

class PortfolioForm(forms.ModelForm):
    class Meta:
        model  = Resume
        fields = ['name', 'theme']

#----------------SECTION FORM ---------------

class SectionForm(forms.ModelForm):
    class Meta:
        model  = Section
        fields = ['title', 'content']