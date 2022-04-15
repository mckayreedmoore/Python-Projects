from django.shortcuts import render
from profiles.models import *

# Create your views here.
def home(request):
    profiles = profiles.objects.all()
    return render(request, 'templates/home.HTML', {'profiles': profile})