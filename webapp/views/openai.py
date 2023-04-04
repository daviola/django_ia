from django.shortcuts import render
from django.contrib import messages

# Create your views here.
linguagens = [
    "c",
    "clike",
    "cpp",
    "csharp",
    "css",
    "csv",
    "django",
    "go",
    "graphql",
    "java",
    "javascript",
    "markup",
    "markup-templating",
    "perl",
    "php",
    "python",
    "ruby",
    "rust",
    "sql",
    "xml-doc",
    "yaml",
    "html",
    ]


def correcao(request):
    params = {
        "view":{
            "id": "correcao",
            "titulo": "Correção de Código"
        },
        "linguagens": linguagens
    }
    if request.method == "POST":
        params["code"] = request.POST.get("code")
        params["linguagem"] = request.POST.get("linguagem")
        if params["linguagem"] == "Selecione a linguagem de programação":
            messages.success(request, "Por favor, selecione uma linguagem.")
            return render(request, "correcao.html", params)
        #aqui vamos fazer um request pra openai
        params["response"] = params["code"]
    return render(request, "correcao.html", params)
