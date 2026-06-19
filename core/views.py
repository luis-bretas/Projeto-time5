from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from movetogether.forms import ActivityForm
def home(request):
    return render(request, 'core/home.html')

def login(request):
    return render(request, 'core/login.html')

def dashboard(request):
    return render(request, 'core/dashboard.html')

def grupo(request):
    return render(request, 'core/grupo.html')

def perfil(request):
    return render(request, 'core/perfil.html')

def ranking(request):
    return render(request, 'core/ranking.html')



@login_required
def registrar_atividade(request):
    if request.method == 'POST':
        form = ActivityForm(request.POST, request.FILES)
        if form.is_valid():
            activity = form.save(commit=False)
            activity.user = request.user
            activity.points_earned = 100 + (activity.duration_minutes // 10)
            activity.save()
            messages.success(request, f'Atividade registrada! +{activity.points_earned} pontos')
            return redirect('dashboard')
    else:
        form = ActivityForm()
    
    return render(request, 'movetogether/registrar_atividade.html', {'form': form})