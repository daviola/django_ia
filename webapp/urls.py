from django.contrib import admin
from django.urls import path
from webapp.views import openai
from webapp.views import autenticacao

urlpatterns = [    
    path("correcao", openai.correcao, name="correcao"),
    path("criacao", openai.criacao, name="criacao"),
    path("geral", openai.geral, name="geral"),
    path("historico", openai.historico, name="historico"),
    path("signin", autenticacao.signin, name="signin"),
    path("signout", autenticacao.signout, name="signout"),
    path("registro", autenticacao.signup, name="registro"),
]
