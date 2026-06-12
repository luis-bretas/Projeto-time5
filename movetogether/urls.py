from django.contrib import admin
from django.urls import path
from core.views import home, login, dashboard, grupo, perfil, ranking
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('login/', login),
    path('dashboard/', dashboard),
    path('grupo/', grupo),
    path('perfil/', perfil),
    path('ranking/', ranking),
    path('accounts/', include('django.contrib.auth.urls')),
]
