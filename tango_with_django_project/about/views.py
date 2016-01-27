from django.shortcuts import render

from django.http import HttpResponse

def about(request):
    return HttpResponse('Rango says hey <a href="/rango/">Index</a> page!')
