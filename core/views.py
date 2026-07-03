from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from movetogether.forms import ActivityForm
from .models import Activity, Group
from django.contrib.auth.models import User
from django.db.models import Sum
from django.contrib.auth import logout


def home(request):
    habilidades = [
        {"emoji": "⭐", "nome": "Iniciante", "descricao": "Até 500 pontos"},
        {"emoji": "🏅", "nome": "Intermediário", "descricao": "Entre 500 e 1500 pontos"},
        {"emoji": "🏆", "nome": "Avançado", "descricao": "Mais de 1500 pontos"}
    ]

    return render(request, 'core/home.html', {"habilidades": habilidades})

def login(request):
    return render(request, 'registration/login.html')
@login_required
def dashboard(request):

    usuario = request.user
    grupo = Group.objects.first()

    atividades = Activity.objects.all().order_by('-created_at')

    atividades_usuario = Activity.objects.filter(user=usuario)

    total_pontos = atividades_usuario.aggregate(
        total=Sum('points_earned')
    )['total'] or 0

    dias_ativos = len(set(
        atividade.created_at.date() for atividade in atividades_usuario
    ))

    ranking_usuarios = User.objects.annotate(
        total_pontos=Sum('activities__points_earned')
    ).filter(
        total_pontos__isnull=False
    ).order_by('-total_pontos')

    posicao = "-"

    for indice, user in enumerate(ranking_usuarios, start=1):
        if user == usuario:
            posicao = f"{indice}º"

    return render(
        request,
        'core/dashboard.html',
        {
            "usuario": usuario,
            "atividades": atividades,
            "total_pontos": total_pontos,
            "dias_ativos": dias_ativos,
            "posicao": posicao,
            "grupo": grupo,
        }
    )

def grupo(request):

    grupo = Group.objects.first()

    if grupo:
        atividades = Activity.objects.filter(group=grupo).order_by('-created_at')
    else:
        atividades = Activity.objects.none()

    membros = User.objects.all()

    total_pontos = atividades.aggregate(
        total=Sum('points_earned')
    )['total'] or 0

    ranking_usuarios = User.objects.filter(
        activities__group=grupo
    ).annotate(
        total_pontos=Sum('activities__points_earned')
    ).order_by('-total_pontos')

    return render(
        request,
        'core/grupo.html',
        {
            "grupo": grupo,
            "atividades": atividades,
            "membros": membros,
            "total_pontos": total_pontos,
            "ranking_usuarios": ranking_usuarios,
        }
    )
@login_required
def perfil(request):

    usuario = request.user

    atividades = Activity.objects.filter(
        user=usuario
    ).order_by('-created_at')

    total_pontos = atividades.aggregate(
        total=Sum('points_earned')
    )['total'] or 0

    total_treinos = atividades.count()

    total_grupos = atividades.values('group').distinct().count()

    dias_ativos = len(set(
        atividade.created_at.date() for atividade in atividades
    ))

    return render(
        request,
        'core/perfil.html',
        {
            "usuario": usuario,
            "atividades": atividades,
            "total_pontos": total_pontos,
            "total_treinos": total_treinos,
            "total_grupos": total_grupos,
            "dias_ativos": dias_ativos,
        }
    )

def ranking(request):

    ranking_usuarios = User.objects.annotate(
        total_pontos=Sum('activities__points_earned')
    ).filter(
        total_pontos__isnull=False
    ).order_by('-total_pontos')

    return render(
        request,
        'core/ranking.html',
        {"ranking_usuarios": ranking_usuarios}
    )
@login_required
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
def sair(request):
    logout(request)
    return redirect('/login/')
