from django import forms
from .models import Pedido
from ..estoque.models import EstoqueItens


class PedidoForm(forms.ModelForm):

    class Meta:
        model = Pedido
        fields = '__all__'


class PedidoItensForm(forms.ModelForm):

    class Meta:
        model = EstoqueItens
        fields = '__all__'
