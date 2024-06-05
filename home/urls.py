from . import views
from django.urls import path




urlpatterns = [
    path('',views.home, name="home"),
    path('kontakt/', views.kontakt, name="kontakt"),
    path('onama/', views.onama, name="onama"),
    path('proizvodi/', views.proizvodi, name="proizvodi"),
    path('tehnologija/', views.tehnologija, name="tehnologija"),
    path('blog/', views.blog, name="blog"),
    path('usluge/', views.usluge, name="usluge"),


    path('testiraj_usera/', views.testiraj_usera, name="testiraj_usera"),
    path('login/', views.login, name="login"),


    path('comming_soon', views.comming_soon, name="comming_soon"),
] 

