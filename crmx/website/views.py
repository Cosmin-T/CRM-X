from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record
from django.http import HttpResponse
from django.views.decorators.http import require_POST
import csv

def home(request):
    records = Record.objects.all()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Authentication successful!")
            return redirect ('home')
        else:
            messages.success(request, "Authentication failed, try again.")
            return redirect ('home')
    else:
        return render(request, 'home.html', {'records':records})


def logout_user(request):
    logout(request)
    messages.success(request, "Logout successful!")
    return redirect ('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Account created successfully!")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})

    return render(request, 'register.html', {'form':form})


def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record':customer_record})
    else:
        messages.success(request, "Not authenticated! Please login.")
        return redirect ('home')

def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Record deleted successfully!")
        return redirect ('home')
    else:
        messages.success(request, "Not authenticated! Please login.")
        return redirect ('home')

def add_record(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = AddRecordForm(request.POST)
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record Added Successfully")
            else:
                messages.error(request, "Invalid form data. Please check the fields.")
        else:
            form = AddRecordForm(initial={'first_name': request.user.first_name, 'last_name': request.user.last_name, 'email': request.user.email})

        return render(request, 'add_record.html', {'form': form})
    else:
        messages.error(request, "Not authenticated! Please login.")
        return redirect('home')

def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record updated successfully!")
            return redirect('home')
        return render(request, 'update_record.html', {'form':form})
    else:
        messages.success(request, "Not authenticated! Please login.")
        return redirect('home')

def download_table(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="table.csv"'

    writer = csv.writer(response)
    records = Record.objects.all()
    writer.writerow(['ID', 'Added Date', 'Name', 'Subject', 'Email', 'Status', 'Resolution', 'Description', 'Comment'])
    for record in records:
        writer.writerow([record.id, record.created_at, f'{record.first_name} {record.last_name}', record.subject, record.email, record.status, record.resolution, record.description, record.comment])

    return response

def delete_all_records(request):
    if request.method == 'POST':
        records = Record.objects.all()
        records.delete()
        messages.success(request, "All records deleted successfully!")
        return redirect ('home')