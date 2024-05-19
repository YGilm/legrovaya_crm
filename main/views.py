from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect


def index(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            return redirect('home')
        else:
            return HttpResponse(f"Введены не корректные данные")
    return render(request, 'main/index.html')


def crm_home(request):
    return render(request,'main/crm_home.html')
