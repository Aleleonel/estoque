from django.contrib import admin
from .models import PedidoSaida, Pedido, PedidoItens


class PedidoItensInline(admin.TabularInline):
    model = PedidoItens
    extra = 0


@admin.register(Pedido)
class EstoqueAdmin(admin.ModelAdmin):
    inlines = (PedidoItensInline,)
    list_display = ('__str__', 'funcionario',)
    search_fields = ('id',)
    list_filter = ('funcionario',)
    date_hierarchy = 'created'


@admin.register(PedidoSaida)
class PedidoSaidaAdmin(admin.ModelAdmin):
    inlines = (PedidoItensInline,)
    list_display = ('__str__', 'funcionario',)
    search_fields = ('id',)
    list_filter = ('funcionario',)
    date_hierarchy = 'created'
