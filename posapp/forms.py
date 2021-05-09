from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model=Item
        fields = ('item_name','item_price','stock_quantity')
        labels = {
            'item_name': 'Item Name',
            'item_price': 'Item Price',
            'stock_quantity': 'Stock Quantity',
        }