from tkinter import Widget
from django import forms
from .models import Books,Category


class Categoryform(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name',]
        widgets= {
            'name':forms.TextInput(attrs={'class':'form-control'})
        }

class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = [
            'title',
            'auther',
            'book_pic',
            'auther_pic',
            'pages',
            'price',
            'rental_price',
            'rental_period',
            'total_rentalprice',
            'status',
            'category',
        ]
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'auther':forms.TextInput(attrs={'class':'form-control'}),
            'book_pic':forms.FileInput(attrs={'class':'form-control'}),
            'auther_pic':forms.FileInput(attrs={'class':'form-control'}),
            'pages':forms.NumberInput(attrs={'class':'form-control'}),
            'price':forms.NumberInput(attrs={'class':'form-control'}),
            'rental_price':forms.NumberInput(attrs={'class':'form-control','id':'rentalprice'}),
            'rental_period':forms.NumberInput(attrs={'class':'form-control','id':'rentalperiod'}),
            'total_rentalprice':forms.NumberInput(attrs={'class':'form-control','id':'totalprice'}),
            'status':forms.Select(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class':'form-control'}),
        }