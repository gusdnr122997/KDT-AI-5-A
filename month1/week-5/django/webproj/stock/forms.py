from django import forms
from .models import Coffee, Burger

class CoffeeForm(forms.ModelForm):
    class Meta:
        model = Coffee
        fields = ('name', 'price', 'is_ice', 'stock')