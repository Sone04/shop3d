from django.shortcuts import render

# Create your views here.

def home (request):

    return render(request, 'home/home.html')

def kontakt (request):

    return render(request, 'home/kontakt.html')

def onama (request):

    return render(request, 'home/onama.html')

def proizvodi (request):

    return render(request, 'home/proizvodi.html')

def tehnologija (request):

    return render(request, 'home/tehnologija.html')

def usluge (request):

    return render(request, 'home/usluge.html')

def blog (request):

    return render(request, 'home/blog.html')
