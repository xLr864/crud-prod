from django import forms
from django.db.models import fields
from .models import Product

class Games_Review(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets ={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.TextInput(attrs={'class':'form-control'}),
            'price':forms.NumberInput(attrs={'class':'form-control'}),
            'summary':forms.TextInput(attrs={'class':'form-control'})
        }