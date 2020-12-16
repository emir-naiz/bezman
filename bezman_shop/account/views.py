from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .decorators import admin_only
from .models import *
from .forms import UserProfile
# Create your views here.

@admin_only
def customerList(request):
    customers = Customer.objects.all()
    context = {'customers': customers}
    return render(request, 'account/customers.html', context)

def getCustomer(request, customer_id):
    try:
        customer = Customer.objects.get(id=customer_id)
    except Customer.DoesNotExist:
        return HttpResponse('Page status = 404')

    orders = customer.order_set.all()
    context = {'customer': customer, 'orders': orders}
    return render(request, 'account/getcustomer.html', context)

def createUser(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='bezgirl')
            user.groups.add(group)
            Customer.objects.create(user=user, phone=1, full_name=user.username)
            user.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'account/user-create.html', context)

def auth(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('products')
    context = {}
    return render(request, 'account/login.html', context)

def logout_page(request):
    logout(request)
    return redirect('login')

@login_required(login_url=['login'])
def userProfile(request):
    user = request.user.customer
    form = UserProfile(instance=user)
    if request.method == 'POST':
        form = UserProfile(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'account/profile.html', context)