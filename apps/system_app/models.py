from django.db import models
from django.conf import settings

class Barbearia(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField(blank=True, null=True)
    endereco = models.CharField(max_length=255)
    nota = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    foto = models.ImageField(upload_to='barbearias/', blank=True, null=True)

    def __str__(self):
        return self.nome


class Barbeiro(models.Model):
    barbearia = models.ForeignKey(Barbearia, on_delete=models.CASCADE, related_name="barbeiros", null=True, blank=True)
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

