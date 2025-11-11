from django.db import models

# app_barbearia/models.py
from django.conf import settings
from django.db import models

class Barbeiro(models.Model):
    nome = models.CharField(max_length=100)
    cadeira = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.nome


class Servico(models.Model):
    nome = models.CharField(max_length=100)
    duracao_minutos = models.PositiveIntegerField(default=30)
    preco = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nome


class Agendamento(models.Model):
    STATUS_CHOICES = [
        ('PENDENTE', 'Pendente'),
        ('CONFIRMADO', 'Confirmado'),
        ('CONCLUIDO', 'Concluído'),
        ('CANCELADO', 'Cancelado'),
    ]

    cliente = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='agendamentos'
    )
    barbeiro = models.ForeignKey(Barbeiro, on_delete=models.PROTECT)
    servico = models.ForeignKey(Servico, on_delete=models.PROTECT)
    data = models.DateField()
    hora = models.TimeField()

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='PENDENTE'
    )

    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['data', 'hora']

    def __str__(self):
        return f'{self.cliente} - {self.data} {self.hora} ({self.servico})'

