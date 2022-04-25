from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def pagina_produtos():
    return HttpResponse('Página de produtos')

def celulares():
    return HttpResponse('Página de celulares')