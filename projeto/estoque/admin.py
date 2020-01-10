from django.contrib import admin
from .models import EstoqueItens, Estoque, EstoqueEntrada, EstoqueSaida


class EstoqueItensInline(admin.TabularInline):
    model = EstoqueItens
    extra = 0


# @admin.register(Estoque)
# class EstoqueAdmin(admin.ModelAdmin):
#     inlines = (EstoqueItensInline,)
#     list_display = ('__str__', 'nf', 'funcionario',)
#     search_fields = ('nf',)
#     list_filter = ('funcionario',)
#     date_hierarchy = 'created'


@admin.register(EstoqueEntrada)
class EstoqueEntradaAdmin(admin.ModelAdmin):
    inlines = (EstoqueItensInline,)
    list_display = ('__str__', 'nf', 'funcionario',)
    search_fields = ('nf',)
    list_filter = ('funcionario',)
    date_hierarchy = 'created'


@admin.register(EstoqueSaida)
class EstoqueSaidaAdmin(admin.ModelAdmin):
    inlines = (EstoqueItensInline,)
    list_display = ('__str__', 'nf', 'funcionario',)
    search_fields = ('nf',)
    list_filter = ('funcionario',)
    date_hierarchy = 'created'
