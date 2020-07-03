from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, resolve_url
from django.views.generic import ListView, DetailView
from projeto.produto.models import Produto

from .forms import PedidoItensForm, PedidoForm
from .models import Pedido, PedidoItens
from ..estoque.models import EstoqueSaida


class PedidoDetail(DetailView):
    model = Pedido
    template_name = 'pedido_detail.html'


def dar_baixa_estoque(form):
    # pega os produtos a partir da instancia do formulario(estoque)
    produtos = form.pedidos.all()
    for item in produtos:
        produto = Produto.objects.get(pk=item.produto.pk)
        produto.estoque = item.saldo
        produto.save()
    print('Estoque atualizado com sucesso.')


def estoque_add(request, template_name, movimento, url):
    pedido_form = Pedido()
    item_pedido_formset = inlineformset_factory(
        Pedido,
        PedidoItens,
        form=PedidoItensForm,
        extra=0,
        can_delete=False,
        min_num=1,
        validate_min=True,
    )
    if request.method == 'POST':
        from .forms import PedidoForm
        form = PedidoForm(request.POST, instance=pedido_form, prefix='main')
        formset = item_pedido_formset(
            request.POST,
            instance=pedido_form,
            prefix='pedido'
        )
        if form.is_valid() and formset.is_valid():
            form = form.save(commit=False)
            form.funcionario = request.user
            form.movimento = movimento
            form.save()
            formset.save()
            dar_baixa_estoque(form)
            return {'pk': form.pk}
    else:
        from .forms import PedidoForm
        form = PedidoForm(instance=pedido_form, prefix='main')
        formset = item_pedido_formset(instance=pedido_form, prefix='pedido')
    context = {'form': form, 'formset': formset}
    return context


def pedido_saida_list(request):
    template_name = 'pedido_list.html'
    objects = EstoqueSaida.objects.all()
    context = {
        'object_list': objects,
        'titulo': 'Saída',
        'url_add': 'pedido:pedido_saida_add'
    }
    return render(request, template_name, context)


class PedidoSaidaList(ListView):
    model = EstoqueSaida
    template_name = 'pedido_list.html'

    def get_context_data(self, **kwargs):
        context = super(PedidoSaidaList, self).get_context_data(**kwargs)
        context['titulo'] = 'Saida'
        context['url_add'] = 'pedido:pedido_saida_add'
        return context


def pedido_saida_detail(request, pk):
    template_name = 'pedido_detail.html'
    obj = EstoqueSaida.objects.get(pk=pk)
    context = {
        'object': obj,
        'url_list': 'pedido:pedido_saida_list'
        }
    return render(request, template_name, context)


@login_required
def estoque_saida_add(request):
    template_name = 'pedido_saida_form.html'
    movimento = 's'
    url = 'pedido:pedido_detail'
    context = estoque_add(request, template_name, movimento, url)
    if context.get('pk'):
        return HttpResponseRedirect(resolve_url(url, context.get('pk')))
    return render(request, template_name, context)

