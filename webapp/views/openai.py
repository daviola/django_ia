from django.shortcuts import render

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
        #aqui vamos fazer um request pra openai
        params["response"] = params["code"]
    return render(request, "correcao.html", params)
