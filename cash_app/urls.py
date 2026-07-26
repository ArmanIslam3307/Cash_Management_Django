from django.urls import path
from .views import *

urlpatterns = [
  path('', dashboard,name='dashboard'),
  path('sign_in/', sign_in,name='sign_in'),
  path('sign_up/', sign_up,name='sign_up'),
  path('sign_out/', sign_out,name='sign_out'),
  
  path('cash_list/', cash_list,name='cash_list'),
  path('add_cash/', add_cash,name='add_cash'),
  path('edit_cash/<str:id>/', edit_cash,name='edit_cash'),
  path('delete_cash/<str:id>/', delete_cash,name='delete_cash'),

  path('expence_list/', expence_list,name='expence_list'),
  path('add_expence/', add_expence,name='add_expence'),
  path('edit_expence/<str:id>/', edit_expence,name='edit_expence'),
  path('delete_expence/<str:id>/', delete_expence,name='delete_expence')
]