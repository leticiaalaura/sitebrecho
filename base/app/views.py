from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html', context={"produtos": [
        {"nome": "camiseta rosa", "preco": 49.90, "descricao":"camisa rosa com gola"},]
                                                 })

 # C:\Users\letic\PycharmProjects\sitebrecho\base\app\templates\homee.html

# C:\Users\letic\PycharmProjects\sitebrecho\base\theme\templates\theme\base.html



