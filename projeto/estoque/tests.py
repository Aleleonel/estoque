from django.test import TestCase

from .models import Estoque, EstoqueEntrada


def estoque_entrada_list(request):
    template_name = 'estoque_entrada_list.html'
    objects = Estoque.objects.all()
    context = {'object_list': objects}
    print(context)