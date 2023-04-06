from django.shortcuts import render
from django.contrib import messages
import openai
from webapp.models import Registros
OPENAI_KEY = "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"
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
        openai.api_key = OPENAI_KEY
        openai.Model.list()
        try:
            response = openai.Completion.create(
                engine = "text-davinci-003",
                prompt = f"Respond only with code. Fix this {params['linguagem']} code: {params['code']}.",
                temperature = 0,
                max_tokens = 1000,
                top_p = 1.0,
                frequency_penalty = 0.0,
                presence_penalty = 0.0
            )
            params["response"] = response["choices"][0]["text"].strip()

            # Salva o registro no historico
            registro = Registros(
                pergunta=params["code"],
                resposta=params["response"],
                linguagem=params["linguagem"],
                user=request.user,
                tipo=params["view"]["id"],
            )
            registro.save()
        except Exception as e:
            params["code"] = e
    return render(request, "correcao.html", params)

def criacao(request):
    params = {
        "view":{
            "id": "criacao",
            "titulo": "Criação de Código"
        },
        "linguagens": linguagens
    }
    if request.method == "POST":
        params["code"] = request.POST.get("code")
        params["linguagem"] = request.POST.get("linguagem")
        if params["linguagem"] == "Selecione a linguagem de programação":
            messages.success(request, "Por favor, selecione uma linguagem.")
            return render(request, "criacao.html", params)
        #aqui vamos fazer um request pra openai
        openai.api_key = OPENAI_KEY
        openai.Model.list()
        try:
            response = openai.Completion.create(
                engine = "text-davinci-003",
                prompt = f"Respond only with code. {params['code']} in {params['linguagem']}.",
                temperature = 0,
                max_tokens = 1000,
                top_p = 1.0,
                frequency_penalty = 0.0,
                presence_penalty = 0.0
            )
            params["response"] = response["choices"][0]["text"].strip()
            # Salva o registro no historico
            registro = Registros(
                pergunta=params["code"],
                resposta=params["response"],
                linguagem=params["linguagem"],
                user=request.user,
                tipo=params["view"]["id"],
            )
            registro.save()
        except Exception as e:
            params["code"] = e
    return render(request, "criacao.html", params)

def geral(request):
    params = {
        "view":{
            "id": "geral",
            "titulo": "Perguntas Gerais"
        },
    }
    if request.method == "POST":
        params["code"] = request.POST.get("code")
        #aqui vamos fazer um request pra openai
        openai.api_key = OPENAI_KEY
        openai.Model.list()
        try:
            response = openai.Completion.create(
                engine = "text-davinci-003",
                prompt = f"{params['code']}.",
                temperature = 0,
                max_tokens = 1000,
                top_p = 1.0,
                frequency_penalty = 0.0,
                presence_penalty = 0.0
            )
            params["response"] = response["choices"][0]["text"].strip()
            # Salva o registro no historico
            registro = Registros(
                pergunta=params["code"],
                resposta=params["response"],
                linguagem="geral",
                user=request.user,
                tipo=params["view"]["id"],
            )
            registro.save()
        except Exception as e:
            params["code"] = e
    return render(request, "geral.html", params)

def historico(request):
    registros = Registros.objects.filter(user_id=request.user.id)
    params = {
        "titulo": "Historico",
        "registros": registros
    }

    return render(request, "historico.html", params)