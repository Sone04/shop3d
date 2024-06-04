from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout

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


def testiraj_usera(request):

    korisnik = request.user

    if not korisnik.is_authenticated:
        return redirect('login')
    
    if korisnik.is_authenticated:
        return redirect('home')
    
def login (request):


    context = {}
    if request.method == 'POST':
        ime = request.POST.get('korisnicko_ime')
        lozinka = request.POST.get('lozinka')

        korisnik = authenticate(request, username=ime, password=lozinka)


        if korisnik is not None:
            auth_login(request, korisnik)
            return redirect('home')  # Preusmeri na željenu stranicu nakon prijave
        else:
            context['error'] = 'Pogrešno korisničko ime ili lozinka.'

    if not context:
        context = None



    return render(request, 'home/login.html', context)

    