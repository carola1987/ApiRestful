from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer
from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse("<h1>Bienvenido a la API RESTful</h1><p>Usa <code>/api/</code> para acceder a los endpoints.</p>")


class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
