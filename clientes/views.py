from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'clientes/index.html')
    #return HttpResponse('Página de clientes')

def emails(request):
    return render(request, 'clientes/email.html')