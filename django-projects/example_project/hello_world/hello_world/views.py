from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    profiles = profiles.objects.all()
    return render(request, 'templates/home.HTML', {'profiles': profile})

