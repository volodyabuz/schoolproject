from django.shortcuts import render
from .models import *

def index(request):
    return render(request, 'kidsedu/index2.html')

def all_posts(request):
    progs = ProgramEdu.objects.all()
    return render(request, 'kidsedu/all_classes.html', context={'progs': progs})
