from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (ListView, DeleteView,CreateView,
UpdateView,DetailView)
from django.contrib import messages
from .models import Produto

def home(request):
    context = {
        'titulo' : "Bem-Vindo ao site !!!!!"
    }

    return render(request, 'home.html', context)


class ProdutoTabelaListView(ListView):
    model = Produto
    template_name = 'estoque/produto_tabela_list.html' 
    context_object_name = 'produtos'
    ordering = ['nome']

class ProdutoDetailView(DetailView):
    model = Produto
    template_name = 'estoque/produto_tabela_detail.html'
    context_object_name = 'produtos'
    
