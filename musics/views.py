from django.shortcuts import render
from django.views.generic import *
from .models import *

# Create your views here.

def music(request):
    if 'q' in request.GET:
        q = request.GET['q']
        musics = Music.objects.filter(siger__icontains=q)

    else:        
        musics = Music.objects.all()

    context = {
        'musics': musics,
    }

    return render(request, 'musics/list.html', context)