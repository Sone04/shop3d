from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse

# Create your views here.

def home (request):

    if request.user.is_authenticated:
        korisnicko_ime = request.user.username
        email = request.user.email
    else:
        korisnicko_ime = ''
        email = ''
        

   
    context = {'korisnicko_ime':korisnicko_ime, 'email':email}

    return render(request, 'home/home.html', context)

def kontakt (request):

    korisnicko_ime = request.user.username
    email = request.user.email

    context = {'korisnicko_ime':korisnicko_ime, 'email':email}

    return render(request, 'home/kontakt.html', context)

def onama (request):

    korisnicko_ime = request.user.username
    email = request.user.email

    context = {'korisnicko_ime':korisnicko_ime, 'email':email}

    return render(request, 'home/onama.html', context)

def proizvodi (request):

    korisnicko_ime = request.user.username
    email = request.user.email

    context = {'korisnicko_ime':korisnicko_ime, 'email':email}

    return render(request, 'home/proizvodi.html', context)

def tehnologija (request):

    korisnicko_ime = request.user.username
    email = request.user.email

    context = {'korisnicko_ime':korisnicko_ime, 'email':email}

    return render(request, 'home/tehnologija.html', context)

def usluge (request):

    korisnicko_ime = request.user.username
    email = request.user.email

    context = {'korisnicko_ime':korisnicko_ime, 'email':email}

    return render(request, 'home/usluge.html', context)

def blog (request):

    korisnicko_ime = request.user.username
    email = request.user.email

    context = {'korisnicko_ime':korisnicko_ime, 'email':email}

    return render(request, 'home/blog.html', context)


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


def comming_soon(request):

    korisnicko_ime = request.user.username
    email = request.user.email

    context = {'korisnicko_ime':korisnicko_ime, 'email':email}

    return render(request, 'home/comming_soon.html', context)


def logout_view(request):

    logout(request)

    return redirect('home')



    