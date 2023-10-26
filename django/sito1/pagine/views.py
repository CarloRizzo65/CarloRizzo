from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("""\
<nav>
<a href='/'>Home</a> | <a href='/chi_siamo/'>Chi siamo</a> |<a href='/contatti/'>Contatti</a>
</nav><h2>Benvenuto sul mio sito!</2>""")

def chi_siamo(request):
    return HttpResponse("""\
<nav>
    <a href='/'>Home</a> | <a href='/chi_siamo/'>Chi siamo</a> | <a href='/contatti/'>Contatti</a>
</nav>
<h2>Societ&agrave; Carlo Rizzo</h2>
<p>Consulenze informatiche a prezzi economici</p>
""")

def contatti(request):
    return HttpResponse("""\
<nav>
    <a href='/'>Home</a> | <a href='/chi_siamo/'>Chi siamo</a> | <a href='/contatti/'>Contatti</a>
</nav>
<h2 style="text-align:center">Contatti</h2>
<div style="margin:auto;padding-left:30px;width:350px;background-color:#aaffaa;border:1px solid #080;border-radius: 10px;">
<p style="text-align:center">Compila il form</p>
<form method="post" action="">
    <label for="oggetto"; style="display:inline-block;width:150px">Oggetto: </label><input type="text" style="width:150px;margin-bottom:30px" name="oggetto" id="oggetto"><br />
    <label for="messaggio"; style="display:inline-block;width:150px;vertical-align:top">Messaggio: </label><textarea rows=4 style="width:150px" name="messaggio" id="oggetto"></textarea></br />
    <button style="display:block;margin:30px auto" type="submit">Invia</button>
</div>
</form>                    
""")