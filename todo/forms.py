from django import forms
from .models import Item

# This will let Django create a form for us.
class ItemForm(forms.ModelForm):
    class Meta: # this gives the form information about itself
        model = Item
        fields = ['name', 'done']
        