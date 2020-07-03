from django.urls import path, include
from projeto.pedido import views as v

app_name = 'pedido'

entrada_patterns = [
    # path('', v.EstoqueEntradaList.as_view(), name='pedido_entrada_list'),
    # # path('add/', v.estoque_entrada_add, name='estoque_entrada_add'),
]

saida_patterns = [
    path('', v.PedidoSaidaList.as_view(), name='pedido_saida_list'),
    path('add/', v.estoque_saida_add, name='pedido_saida_add'),
]

urlpatterns = [
    path('<int:pk>/', v.PedidoDetail.as_view(), name='pedido_detail'),
    path('entrada/', include(entrada_patterns)),
    path('saida/', include(saida_patterns)),
]
