from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from base.app.models import Produto

def home(request):
    produtos = {'produtos': Produto.objects.all()}
    return render(request, 'home.html', context=produtos)


