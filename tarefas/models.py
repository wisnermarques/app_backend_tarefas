from django.db import models

# Create your models here.

class Tarefa(models.Model):
    STATUS_CHOICES = [
        ('Pendente', 'Pendente'),
        ('Em andamento', 'Em andamento'),
        ('Concluída', 'Concluída'),
    ]

    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pendente')
    dataInicio = models.DateField()
    dataFim = models.DateField()

    def __str__(self):
        return self.nome