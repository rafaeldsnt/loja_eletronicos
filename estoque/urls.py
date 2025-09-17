from django.urls import path
from . import views

app_name = 'estoque'

urlpatterns = [
    path('', views.home, name='home'),
    path('produtos/listar/', views.ProdutoTabelaListView.as_view(), name='listprod'),
]