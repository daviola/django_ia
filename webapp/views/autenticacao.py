from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def signin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Você logou com sucesso")
            return redirect("correcao")
        else:
            messages.success(request, "Falha ao efetuar login")
            return redirect("correcao")
    return render(request, "correcao.html")


def signout(request):
    logout(request)
    messages.success(request, "Você efetuou logout")
    return redirect("correcao")

def signup(request):
    pass