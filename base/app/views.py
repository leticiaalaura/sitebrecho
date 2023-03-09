from django.shortcuts import render

# Create your views here.
from base.app.models import Produto

def home(request):
    produtos = {'produtos': Produto.objects.all()}
    return render(request, 'theme/base.html', context=produtos)


