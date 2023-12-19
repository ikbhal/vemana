# poems/views.py
from django.shortcuts import render
from .models import Poem

def index(request):
    poems = Poem.objects.all()
    return render(request, 'poems/index.html', {'poems': poems})
