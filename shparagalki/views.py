    # shparagalki/views.py
from django.shortcuts import render # <-- Исправьте эту строку

def index(request):
        return render(request, 'home.html')
    
