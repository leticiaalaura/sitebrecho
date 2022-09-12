from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html', context={"produtos": [
        {"produto": "Blazer listrado", "preco": 59.90, "descricao": "Blazer listrado com forro", "foto": 'img/blazer.png'},
        {"produto": "Vestido menta", "preco": 49.90, "descricao": "Vestido cor menta e estampa Animal Print", "foto": 'img/vestido.png'},
        {"produto": "Saia midi onça", "preco": 69.90, "descricao": "Saia midi tecido listrado estampa onça"},]
                                                 })

 # C:\Users\letic\PycharmProjects\sitebrecho\base\app\templates\homee.html

# C:\Users\letic\PycharmProjects\sitebrecho\base\theme\templates\theme\base.html



