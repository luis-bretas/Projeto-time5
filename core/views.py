from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from movetogether.forms import ActivityForm
from .models import Activity, Group
def home(request):
    habilidades = [
        {"emoji": "⭐", "nome": "Iniciante", "descricao": "Até 500 pontos"},
        {"emoji": "🏅", "nome": "Intermediário", "descricao": "Entre 500 e 1500 pontos"},
        {"emoji": "🏆", "nome": "Avançado", "descricao": "Mais de 1500 pontos"}
    ]

    return render(request, 'core/home.html', {"habilidades": habilidades})

def login(request):
    return render(request, 'registration/login.html')

def dashboard(request):
    atividades = Activity.objects.all().order_by('-created_at')

    return render(
        request,
        'core/dashboard.html',
        {"atividades": atividades}
    )

def grupo(request):

    membros = [
        "Theo",
        "Luís",
        "Ana",
        "João"
    ]

    return render(
        request,
        'core/grupo.html',
        {"membros": membros}
    )

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

def atividade(request):

    mensagem = ""

    if request.method == "POST":

        nome = request.POST.get("nome")
        tipo = request.POST.get("tipo")
        pontos = request.POST.get("pontos")
        descricao = request.POST.get("descricao")
        duracao = request.POST.get("duracao")

        grupo = Group.objects.first()

        if request.user.is_authenticated and grupo:
            Activity.objects.create(
                user=request.user,
                group=grupo,
                description=descricao or nome,
                duration_minutes=duracao or 0,
                points_earned=pontos or 0
            )

            mensagem = f"Atividade '{nome}' enviada e salva no banco com sucesso! (+{pontos} pontos)"

        else:
            mensagem = "Erro: é necessário estar logado e ter um grupo cadastrado."

    return render(
        request,
        'core/atividade.html',
        {"mensagem": mensagem}
    )