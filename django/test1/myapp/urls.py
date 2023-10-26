#In questo file gestisco le path dell view dell'app
from django.urls import path #Richiamo il metodo path di django

from . import views #importo la classe view dell'app

urlpatterns = [
    path('', views.index, name='index'),
    path('giuseppe/', views.carlo, name='carlo')
]