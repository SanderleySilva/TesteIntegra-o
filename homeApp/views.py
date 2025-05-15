from django.shortcuts import render
from produtosApp.models import ProdutosCad

def homePage(request):
    produtos = ProdutosCad.objects.all()
    return render(request, 'home.html', {'produtos':produtos})
