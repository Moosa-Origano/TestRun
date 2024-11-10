from django.shortcuts import render
from django.http import HttpResponse

# request --> response

def calculate():
    x = 1
    y = 2
    return x


def say_hello(request):
    # Do pretty much anything
    x = calculate()
    return render(request, "hello.html", {'name': 'Marsh'})


def showtext(request):
    return render(request, "showtext.html")