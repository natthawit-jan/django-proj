from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, "hello/index.html")


def greet(request, name):
    return render(request, "hello/greet.html", {"name": name})


def natwit(request):
    return HttpResponse("Hello Natwit")


def yodyiam(request):
    return HttpResponse("Hello Yodyiam")
