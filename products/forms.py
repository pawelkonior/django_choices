from django import forms

from . import models


class ProductForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = ('name', 'prize', 'description', 'category', 'subcategory')


class ProductFormCustom(forms.Form):
    name = forms.CharField(label='Name')
    prize = forms.DecimalField(label='Price')
    description = forms.CharField(label='Description')
    category = forms.ChoiceField(label='Category', choices=tuple())
    subcategory = forms.MultipleChoiceField(label='Subcategory', choices=tuple())
