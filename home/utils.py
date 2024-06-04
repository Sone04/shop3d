import json
from .models import *

def cookieKorpa(request):

	#Create empty cart for now for non-logged in user
	try:
		korpa = json.loads(request.COOKIES['korpa'])
	except:
		korpa = {}
		print('KORPA:', korpa)

	proizvodi = []
	narudzbina = {'izracunaj_ukupnu_cenu':0, 'dodati_proizvodi':0}
	proizvodiUKorpi = narudzbina['dodati_proizvodi']

	for i in korpa:
		#We use try block to prevent items in cart that may have been removed from causing error
		try:	
			if(korpa[i]['quantity']>0): #items with negative quantity = lot of freebies  
				proizvodiUKorpi += korpa[i]['quantity']

				proizvod = Proizvod.objects.get(id=i)
				ukupno = (proizvod.cena * korpa[i]['quantity'])

				narudzbina['izracunaj_ukupnu_cenu'] += ukupno
				narudzbina['dodati_proizvodi'] += korpa[i]['quantity']

				proizvod = {
				'id':proizvod.id,
				'proizvod':{'id':proizvod.id,'name':proizvod.ime, 'cena':proizvod.cena, 
				'imageURL':proizvod.imageURL}, 'quantity':korpa[i]['quantity'],
				'izracunaj_ukupno':ukupno,
				}
				proizvodi.append(proizvod)

		except:
			pass
			
	return {'proizvodiUKorpi':proizvodiUKorpi ,'narudzbina':narudzbina, 'proizvodi':proizvodi}

def informacijeKorpe(request):
	if request.user.is_authenticated:
		korisnik = request.user.korisnik
		narudzbina, created = Narudzbina.objects.get_or_create(korisnik=korisnik, complete=False)
		proizvodi = narudzbina.narucenproizvod_set.all()
		proizvodiUKorpi = narudzbina.dodati_proizvodi
	else:
		cookieInformacije = cookieKorpa(request)
		proizvodiUKorpi = cookieInformacije['proizvodiUKorpi']
		narudzbina = cookieInformacije['narudzbina']
		proizvodi = cookieInformacije['proizvodi']

	return {'proizvodiUKorpi':proizvodiUKorpi ,'narudzbina':narudzbina, 'proizvodi':proizvodi}

	
def gostNarudzbina(request, data):
	ime = data['form']['ime']
	email = data['form']['email']

	cookieInformacije = cookieKorpa(request)
	proizvodi = cookieInformacije['proizvodi']

	korisnik, created = Korisnik.objects.get_or_create(
			email=email,
			)
	korisnik.ime = ime
	korisnik.save()

	narudzbina = Narudzbina.objects.create(
		korisnik=korisnik,
		zavrsena=False,
		)

	for proizvod in proizvodi:
		proizvod = Proizvod.objects.get(id=proizvod['id'])
		narucenproizvod = NarucenProizvod.objects.create(
			proizvod=proizvod,
			narudzbina=narudzbina,
			kolicina=(proizvod['quantity'] if proizvod['quantity']>0 else -1*proizvod['quantity']), # negative quantity = freebies
		)
	return korisnik, narudzbina

