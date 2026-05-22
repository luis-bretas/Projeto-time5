

# Register your models here.
from django.contrib import admin
from .models import Usuario, Grupo, Atividade

admin.site.register(Usuario)
admin.site.register(Grupo)
admin.site.register(Atividade)