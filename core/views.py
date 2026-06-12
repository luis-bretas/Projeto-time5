from django.shortcuts import render

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