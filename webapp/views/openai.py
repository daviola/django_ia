from django.shortcuts import render

# Create your views here.
linguagens = [
    'c',
    'clike',
    'cpp',
    'csharp',
    'css',
    'csv',
    'django',
    'go',
    'graphql',
    'java',
    'javascript',
    'markup',
    'markup-templating',
    'perl',
    'php',
    'python',
    'ruby',
    'rust',
    'sql',
    'xml-docyamlhtml'
    ]


def correcao(request):
    params = {
        "view":{
            "id": "correcao",
            "titulo": "Correção de Código"
        },
        "linguagens": linguagens
    }
    return render(request, "correcao.html", params)
