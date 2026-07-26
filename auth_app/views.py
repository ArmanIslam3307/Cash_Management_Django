from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

from .forms import *

# Create your views here.
@login_required
def dashboard(req):

  total_cash = AddCash.objects.filter(user=req.user).aggregate(total_amount = Sum('amount'))['total_amount'] or 0
  total_expence = Expense.objects.filter(user=req.user).aggregate(total_amount = Sum('amount'))['total_amount'] or 0

  total = total_cash - total_expence

  context = {
    'total_cash' : total_cash,
    'total_expence' : total_expence,
    'total' : total
  }

  
  return render(req,'dashboard.html',context)


  
def sign_up(req):
  
  if req.method == 'POST':
    username = req.POST.get('username')
    full_name = req.POST.get('full_name')
    email = req.POST.get('email')
    role = req.POST.get('role')
    password = req.POST.get('password')
    conf_password = req.POST.get('conf_password')

    if CustomUser.objects.filter(username=username).exists():
      messages.warning(req,'Username already exists!')
      return redirect('sign_up')
              

    if password == conf_password:
      CustomUser.objects.create_user(
        username=username,
        full_name=full_name,
        email=email,
        role=role,
        password=conf_password
      )
      return redirect('sign_in')
      
  return render(req,'auth/signUp.html')
  
def sign_in(req):
  if req.method == 'POST':
    username = req.POST.get('username')
    password = req.POST.get('password')

    user = authenticate(req,username=username,password=password)

    if user:
      login(req,user)
      return redirect('dashboard')

  return render(req,'auth/signIn.html')

@login_required
def sign_out(req):
  logout(req)
  return redirect('sign_in')
@login_required
def add_cash(req):

  if req.method == 'POST':
    form_data = AddCashForm(req.POST)
    if form_data.is_valid():
      data = form_data.save(commit=False)
      data.user = req.user
      data.save()
      return redirect('cash_list')


  form_data = AddCashForm()

  context = {
    'form_data' : form_data,
    'title' : 'Add Cash Form',
    'btn' : 'Add Cash'
  }

  return render(req,'cash_form.html',context)
@login_required
def cash_list(req):
  data = AddCash.objects.filter(user=req.user)


  context = {
    'data' : data
  }

  return render(req,'cash-list.html', context)
  
@login_required
def edit_cash(req,id):
  data = get_object_or_404(AddCash,id=id)
  if req.method == 'POST':
    form_data = AddCashForm(req.POST,instance=data)
    if form_data.is_valid():
      data = form_data.save(commit=False)
      data.user = req.user
      data.save()
      messages.success(req,'Data Updated Successfully!')
      return redirect('cash_list')


  form_data = AddCashForm(instance=data)

  context = {
    'form_data' : form_data,
    'title' : 'Edit Cash Form',
    'btn' : 'Edit Cash'
  }

  return render(req,'cash_form.html',context)

def delete_cash(req,id):
  data = get_object_or_404(AddCash,id=id)
  data.delete()
  messages.success(req,'Data Deleted Successfully!')
  return redirect('cash_list')
  
def add_expence(req):

  if req.method == 'POST':
    form_data = ExpenseForm(req.POST)
    if form_data.is_valid():
      data = form_data.save(commit=False)
      data.user = req.user
      data.save()
      return redirect('expence_list')


  form_data = ExpenseForm()

  context = {
    'form_data' : form_data,
    'title' : 'Add Expence Form',
    'btn' : 'Add Expence'
  }

  return render(req,'cash_form.html',context)
  
@login_required
def expence_list(req):
  data = Expense.objects.filter(user=req.user)


  context = {
    'data' : data
  }

  return render(req,'expence-list.html', context)

def edit_expence(req,id):
  data = get_object_or_404(Expense,id=id)
  if req.method == 'POST':
    form_data = ExpenseForm(req.POST,instance=data)
    if form_data.is_valid():
      data = form_data.save(commit=False)
      data.user = req.user
      data.save()
      messages.success(req,'Data Updated Successfully!')
      return redirect('expence_list')


  form_data = ExpenseForm(instance=data)

  context = {
    'form_data' : form_data,
    'title' : 'Edit Expence Form',
    'btn' : 'Edit Expence'
  }

  return render(req,'cash_form.html',context)

def delete_expence(req,id):
  data = get_object_or_404(Expense,id=id)
  data.delete()
  messages.success(req,'Data Deleted Successfully!')
  return redirect('expence_list')