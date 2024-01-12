from django.shortcuts import render,redirect, get_object_or_404
from .models import *
# Create your views here.
def home(request):
   profile=Profile.objects.filter(user= request.user).first()
   expenses= Expense.objects.filter(user= request.user)

   if request.method == 'POST':
    text=request.POST.get('text')  
    amount =request.POST.get('amount')
    expense_type=request.POST.get('expense_type')
    
    
    expense= Expense(name=text,amount=amount,expense_type=expense_type,user=request.user)
    expense.save()

    if expense_type=='Positive':
      profile.income+=float(amount)
      profile.balance+=float(amount)

    else:
      profile.expense+=float(amount)
      profile.balance-=float(amount)  


    profile.save()  

  
  
   context = {'profile':profile, 'expenses':expenses} 
   return render(request, 'home.html',context)

