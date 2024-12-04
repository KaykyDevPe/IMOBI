from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . models import Imovel, Cidade

@login_required(login_url='/auth/logar/')
def home(request):
    cidades = Cidade.objects.all()
    imoveis = Imovel.objects.all()
    
    context = {
        'cidades': cidades,
        'imoveis': imoveis
    }
    
    return render(request, 'home.html', context)