from django.shortcuts import render, redirect
from .models import MedicineReminder
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'user' and password == 'user':
            request.session['is_logged_in'] = True
            return redirect('dashboard')
        else:
            return render(request, 'reminders/login.html', {'error': 'Invalid credentials'})
    return render(request, 'reminders/login.html')

def dashboard(request):
    if not request.session.get('is_logged_in'):
        return redirect('login')
    reminders = MedicineReminder.objects.all()
    return render(request, 'reminders/dashboard.html', {'reminders': reminders})

def add_reminder(request):
    if not request.session.get('is_logged_in'):
        return redirect('login')
    if request.method == 'POST':
        medicine_name = request.POST.get('medicine_name')
        date = request.POST.get('date')
        time = request.POST.get('time')
        frequency = request.POST.get('frequency')
        
        MedicineReminder.objects.create(
            medicine_name=medicine_name,
            date=date,
            time=time,
            frequency=frequency
        )
        return redirect('dashboard')
    return render(request, 'reminders/add_reminder.html')

def logout_view(request):
    request.session.flush()
    return redirect('login')
