from rest_framework import serializers
from .models import *

class AddCashSerializer(serializers.ModelSerializer):
  class Meta:
    model = AddCash
    fields = '__all__'
    
class ExpenseSerializer(serializers.ModelSerializer):
  class Meta:
    model = Expense
    fields = '__all__'