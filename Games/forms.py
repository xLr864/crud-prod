from django import forms
from django.db.models import fields
from .models import Review

class Games_Review(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        widgets ={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'ratting':forms.NumberInput(attrs={'class':'form-control'}),
            'verdict':forms.TextInput(attrs={'class':'form-control'})
        }