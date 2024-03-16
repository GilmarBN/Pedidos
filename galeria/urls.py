from django.urls import path
from galeria.views import index, pedidos, novo_pedido

urlpatterns = [
    path('', index, name='index'),
    path('pedidos', pedidos, name='pedidos'),
    path('novo_pedido', novo_pedido, name='novo_pedido'),
]