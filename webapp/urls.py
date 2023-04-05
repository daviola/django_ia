from django.contrib import admin
from django.urls import path
from webapp.views import openai

urlpatterns = [    
    path("correcao", openai.correcao, name="correcao"),
    path("criacao", openai.criacao, name="criacao"),
    path("geral", openai.geral, name="geral"),
]
