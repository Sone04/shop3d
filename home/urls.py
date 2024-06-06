from . import views
from django.urls import path
from django.contrib.auth import views as auth_views




urlpatterns = [
    path('',views.home, name="home"),
    path('comming_soon/', views.comming_soon, name="comming_soon"),
    path('testiraj-usera/', views.testiraj_usera, name='testiraj_usera'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),



    path('kontakt/', views.kontakt, name="kontakt"),
    path('onama/', views.onama, name="onama"),
    path('proizvodi/', views.proizvodi, name="proizvodi"),
    path('tehnologija/', views.tehnologija, name="tehnologija"),
    path('blog/', views.blog, name="blog"),
    path('usluge/', views.usluge, name="usluge"),


    
  
] 

