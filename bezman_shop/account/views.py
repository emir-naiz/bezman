from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
# Create your views here.


def customerList(request):
    customers = Customer.objects.all()
    context = {'customers': customers}
    return render(request, 'account/customers.html', context)

def getCustomer(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    orders = customer.order_set.all()
    context = {'customer': customer, 'orders': orders}
    return render(request, 'account/getcustomer.html', context)

def createUser(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customers')
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

def task1(request):
    string = 'Sunshine'
    list = []
    for i in string:
        letter = set(string)
        if len(letter) % 2 == 0:
            return HttpResponse ("IGNORE HIM" +' '+string)
        else:
            return HttpResponse("CHAT WITH HER!" +' '+string)

def task2(request):
    import random
    n,h = 3,7
    list1 = []
    list2 = [4,5,14]
    # for i in range(n):
    #     list1.append(random.randint(1,20))
    for height in list2:
        if height > h:
          list1.append(2)
        elif height <= h:
          list1.append(1)
    return HttpResponse (sum(list1))

