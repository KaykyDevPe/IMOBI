from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . models import Imovel

@login_required(login_url='/auth/logar/')
def home(request):
    imoveis = Imovel.objects.all()
    return render(request, 'home.html', {'imoveis': imoveis})