from django.shortcuts import render

def index(request):
    return render(request, 'kidsedu/index2.html')
