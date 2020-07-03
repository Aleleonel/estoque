from django.contrib.auth.models import User
from django.db import models
from projeto.core.models import TimeStampedModel
from projeto.produto.models import Produto
from .managers import PedidoSaidaManager
from ..estoque.models import Estoque


class Pedido(TimeStampedModel):
    STATUS_CHOICES = (
        ("O", "Orçamento"),
        ("E", "Efetivado"),
        ("C", "Cancelado"),
    )
    funcionario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    cliente = models.CharField(max_length=60)
    dtpedido = models.DateTimeField(auto_created=True)
    valor = models.FloatField(blank=False, null=False)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, blank=False, null=False)
    movimento = models.CharField(max_length=1, default='s', blank=True)
    observacoes = models.CharField(max_length=300, null=False, blank=False)

    class Meta:
        ordering = ('-created',)


class PedidoSaida(Estoque):

    objects = PedidoSaidaManager()

    class Meta:
        proxy = True
        verbose_name = 'pedido saída'
        verbose_name_plural = 'pedido saída'


class PedidoItens(models.Model):
    estoque = models.ForeignKey(
        Estoque,
        on_delete=models.CASCADE,
        related_name='estoque'
    )
    pedido = models.ForeignKey(
        Pedido,
        on_delete=models.CASCADE,
        related_name='pedidos'
    )
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    saldo = models.PositiveIntegerField(blank=True)

    class Meta:
        ordering = ('pk',)

    def __str__(self):
        return '{} - {} - {}'.format(self.pk, self.estoque.pk, self.produto)
