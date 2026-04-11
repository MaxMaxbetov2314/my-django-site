    # shparagalki/urls.py
from django.urls import path
from . import views # Важно: убедитесь, что перед 'from' нет никаких пробелов!

urlpatterns = [
        path('', views.index, name='index'),
    ]
    
