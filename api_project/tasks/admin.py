from django.contrib import admin
from .models import Task

# Registra el modelo en el admin
admin.site.register(Task)
