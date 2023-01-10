from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib import messages


# Create your views here.


def login_action(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('polls:index')
        else:
            messages.error(request, "Username and password cannot be verified")
            return redirect("users:login")
