    # shparagalki/views.py
from django.shortcuts import render # <-- Исправьте эту строку
from django.contrib.auth.decorators import login_required # Если вы все еще используете HttpResponse для какой-то функции, убедитесь, что она тоже импортирована правильно

@login_required
def index(request):
        return render(request, 'home.html')
    
