from django.db import models


class PedidoSaidaManager(models.Manager):
    def get_queryset(self):
        return super(PedidoSaidaManager, self).get_queryset().filter(movimento='s')
