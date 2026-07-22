from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import MonthlyPayment

def index(request):
    # Get all payments
    payments = MonthlyPayment.objects.all()

    return render(request, 'index.html')
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            print(" Login successful!")
            return redirect('data')
        else:
            print(" Login failed!")
            return render(request, 'login.html', {
                'error_message': 'Invalid username or password'
            })
    return render(request, 'login.html')
def data_view(request):
    # Get ONLY the current logged-in user's payments
    payments = MonthlyPayment.objects.filter(user=request.user)
    
    return render(request, 'data.html', {
        'payments': payments,
        'total_payments': payments.count()
    })
    return render(request, 'login.html')
def logout_view(request):
    logout(request)
    return redirect('index')