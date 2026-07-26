from django import forms

from .models import *

class AddCashForm(forms.ModelForm):
  class Meta:
    model = AddCash
    fields = '__all__'
    exclude = ['user']

    widgets = {
      'datetime' : forms.DateTimeInput(attrs={
        'type' : 'datetime-local'
      })
    }
    
class ExpenseForm(forms.ModelForm):
  class Meta:
    model = Expense
    fields = '__all__'
    exclude = ['user']

    widgets = {
      'datetime' : forms.DateTimeInput(attrs={
        'type' : 'datetime-local'
      })
    }