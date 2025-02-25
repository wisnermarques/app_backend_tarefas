from rest_framework import generics
from .models import Tarefa
from .serializers import TarefaSerializer

# Create your views here.

# View para listar todas as tarefas e criar uma nova tarefa
class TarefaListCreateView(generics.ListCreateAPIView):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer

class TarefaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer

# View para recuperar, atualizar e deletar uma tarefa específica
class TarefaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer
