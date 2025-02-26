from rest_framework import generics, permissions
from .models import Tarefa
from .serializers import TarefaSerializer

# View para listar todas as tarefas e criar uma nova tarefa
class TarefaListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer

# View para recuperar, atualizar e deletar uma tarefa específica
class TarefaDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer