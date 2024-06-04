from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# korik
# proizvod
# narudzbina
# narucen proizvod
# informacija korisnika kom se isporucuje
class Korisnik(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    ime = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)


class Proizvod(models.Model):
    ime = models.CharField(max_length=200)
    cena =  models.FloatField()
    slika = models.ImageField(null=True, blank=True)

    @property
    def imageURL(self):
        try:
            url = self.slika.url
        except:
            url = ''
        return url


class Narudzbina(models.Model):
    korisnik = models.ForeignKey(Korisnik, on_delete=models.SET_NULL, null=True, blank=True)
    datum_narudzbine = models.DateTimeField(auto_now_add=True)
    zavrsena = models.BooleanField(default=False)
    broj_transakcije = models.CharField(max_length=100, null=True)

    @property
    def izracunaj_ukupnu_cenu(self):
        narucen_proizvodi = self.narucenproizvod_set.all()
        ukupno = sum([item.get_total for item in narucen_proizvodi])
        return ukupno 

    @property
    def dodati_proizvodi(self):
        narucen_proizvodi = self.narucenproizvod_set.all()
        ukupno = sum([item.quantity for item in narucen_proizvodi])
        return ukupno 


class NarucenProizvod(models.Model):
    proizvod = models.ForeignKey(Proizvod, on_delete=models.SET_NULL, null=True)
    narudzbina =  models.ForeignKey(Narudzbina, on_delete=models.SET_NULL, null=True)
    kolicina = models.IntegerField(default=0, null=True, blank=True)
    datum_dodavanja = models.DateTimeField(auto_now_add=True)

    @property
    def izracunaj_ukupno(self):
        ukupno = self.proizvod.cena * self.quantity
        return ukupno

class InformacijeIsporuke(models.Model):     
    korisnik = models.ForeignKey(Korisnik, on_delete=models.SET_NULL, null=True, blank=True)
    narudzbina = models.ForeignKey(Narudzbina, on_delete=models.SET_NULL, null=True)
    adresa = models.CharField(max_length=200, null=False)  
    grad = models.CharField(max_length=200, null=False)
    regija = models.CharField(max_length=200, null=False)
    postanski_broj = models.CharField(max_length=200, null=False)
    datum_dodavanja = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return self.adresa 