from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
 #   return render(request, 'base.html')
    return render(request,'index.html')   

def carlo(request):
    #return HttpResponse("<nav><a href='/'>Home</a> | <a href='/carlo/'>Carlo</a></nav>Ciao Mondo! Sono una pagina Python")
    return render(request,'carlo.html') 