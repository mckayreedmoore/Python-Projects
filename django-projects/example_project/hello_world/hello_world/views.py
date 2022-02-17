from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    names = ['John', 'Ben', 'Charles', 'Henry']
    context = {
        'names': names,
    }

    return render(request, 'home.html', context)