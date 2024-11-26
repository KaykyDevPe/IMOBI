from django.shortcuts import render, redirect
from django.http import HttpResponse

def cadastro(request):
    return render(request, 'cadastro.html')

def logar(request):
    pass