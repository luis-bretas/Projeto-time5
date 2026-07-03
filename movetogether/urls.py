from django.contrib import admin
from django.urls import path
from core.views import home, login, dashboard, grupo, perfil, ranking
from django.urls.conf import include
from core.views import home, dashboard, grupo, perfil, ranking, atividade, sair
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('accounts/', include('django.contrib.auth.urls')),
    path('dashboard/', dashboard),
    path('grupo/', grupo),
    path('perfil/', perfil),
    path('ranking/', ranking),
    path('atividade/', atividade),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', sair, name='logout'),
]