from django.shortcuts import render

def home(request):
    habilidades = [
        {"emoji": "⭐", "nome": "Iniciante", "descricao": "Até 500 pontos"},
        {"emoji": "🏅", "nome": "Intermediário", "descricao": "Entre 500 e 1500 pontos"},
        {"emoji": "🏆", "nome": "Avançado", "descricao": "Mais de 1500 pontos"}
    ]

    return render(request, 'core/home.html', {"habilidades": habilidades})

def login(request):
    return render(request, 'core/login.html')

def dashboard(request):
    return render(request, 'core/dashboard.html')

def grupo(request):
    return render(request, 'core/grupo.html')

def perfil(request):
    usuario = {
        "nome": "Luís",
        "pontos": 1250,
        "nivel": "Intermediário",
        "esporte": "Academia"
    }

    return render(request, 'core/perfil.html', {"usuario": usuario})

def ranking(request):
    jogadores = [
        {"posicao": "1º", "nome": "Theo", "pontos": 1500},
        {"posicao": "2º", "nome": "Luís", "pontos": 1250},
        {"posicao": "3º", "nome": "Ana", "pontos": 980},
        {"posicao": "4º", "nome": "João", "pontos": 700},
    ]

    return render(request, 'core/ranking.html', {"jogadores": jogadores})