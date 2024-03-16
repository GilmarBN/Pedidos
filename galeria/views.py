from django.shortcuts import render

def index(request):
    return render(request, 'galeria/index.html')

def novo_pedido(request):
    return render(request, 'galeria/novo_pedido.html')

def pedidos(request):
    return render(request, 'galeria/pedidos.html')