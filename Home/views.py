from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import render


import io
import urllib, base64
import matplotlib.pyplot as plt
from .models import daily_expense_database
from django.contrib import messages  # Import messages module
from datetime import datetime, date
from django.utils import timezone


import celery
# Create your views here.
def index(request):
    return render(request,'home.html')

def daily_report_form(request):
    if request.method == 'POST':
        food = request.POST.get('food')
        rent = request.POST.get('rent')
        entertainment = request.POST.get('entertainment')
        try:
            # Convert input values to appropriate types (integers in this case)
            food = int(food)
            rent = int(rent)
            entertainment = int(entertainment)
        except ValueError:
            # Handle invalid input gracefully (e.g., display an error message)
            messages.error(request, "Please enter valid numbers for expenses.")
            return render(request, 'Daily_report_form.html')
        daily_exp_data=daily_expense_database(food=food,rent=rent,entertainment=entertainment)
        daily_exp_data.created_at=timezone.now()
        daily_exp_data.save()
        # Optionally, you can add a success message
        messages.success(request, 'Expense data saved successfully.')

    return render(request, 'Daily_report_form.html')

def daily_report_result(request):
    if request.method == 'POST':
        # Get today's date
        today_date = date.today()
        # Retrieve today's data from the database
        today_data = daily_expense_database.objects.filter(created_at__date=today_date)
        if today_data.exists():
            # Calculate the values for each category
            food_total = sum(data.food for data in today_data)
            rent_total = sum(data.rent for data in today_data)
            entertainment_total = sum(data.entertainment for data in today_data)
            print(food_total)
            context={
                'food_total': food_total, 
                'rent_total': rent_total,
                'entertainment_total': entertainment_total
            }
            return render(request,'Daily_report_result.html',context)
        else:
            # No data exists for today's date
             print("No data")

    
    
    
    return render(request,'Daily_report_result.html')

