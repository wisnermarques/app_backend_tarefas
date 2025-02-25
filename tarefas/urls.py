from django.urls import path
from .views import TarefaListCreateView, TarefaDetailView

urlpatterns = [
    path('tarefas/', TarefaListCreateView.as_view(), name='tarefa-list-create'),
    path('tarefas/<int:pk>/', TarefaDetailView.as_view(), name='tarefa-detail'),
]