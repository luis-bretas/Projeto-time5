from django.contrib import admin
from django.urls import path
from core.views import home, login, dashboard, grupo, perfil, ranking
from django.urls.conf import include
from core.views import home, login, dashboard, grupo, perfil, ranking, atividade


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('login/', login),
    path('dashboard/', dashboard),
    path('grupo/', grupo),
    path('perfil/', perfil),
    path('ranking/', ranking),
    path('atividade/', atividade),
    path('accounts/', include('django.contrib.auth.urls')),
]
from django.conf import settings
from django.conf.urls.static import static

# ... urlpatterns existentes ...
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('movetogether/', include('movetogether.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)