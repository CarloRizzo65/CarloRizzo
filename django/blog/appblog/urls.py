#In questo file gestisco le path dell view dell'app
from django.urls import path #Richiamo il metodo path di django

from . import views #importo la classe view dell'app

urlpatterns = [
    path('', views.index, name='index'),
    path('autore1/', views.autore1, name='autore1'),
    path('autore2/', views.autore2, name='autore2'),
    path('contatti/', views.contatti, name='contatti')
]