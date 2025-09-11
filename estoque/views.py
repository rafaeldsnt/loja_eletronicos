from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (ListView, DeleteView,CreateView,
UpdateView,DetailView)
from django.contrib import messages

def home(request):

    context = {
        'titulo' : "Bem-Vindo ao site !!!!!"
    }

    return render(request, 'home.html', context)