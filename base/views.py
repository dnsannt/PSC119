from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def main(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    # return render(request, 'index.html')
    return render(request, 'main.html')


def index2(request):
    return render(request, 'base/index2.html')


def index3(request):
    return render(request, 'base/index3.html')
