from django.shortcuts import render

# Create your views here.

def correcao(request):
    params = {
        "view":{
            "id": "correcao",
            "titulo": "Correção de Código"
        }
    }
    return render(request, "correcao.html", params)
