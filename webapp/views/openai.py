from django.shortcuts import render

# Create your views here.

def correcao(request):
    return render(request, "correcao.html", {"teste": "teste123"})
