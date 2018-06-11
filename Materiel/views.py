from django.shortcuts import render
from django.http import HttpResponse

def Accueil(request) :

	return render(request, 'Materiel.html')

def Optiques(request) :

	return render(request, 'Optiques.html')

def Monture(request) :

	return render(request, 'Monture.html')

def Capteurs(request) :

	return render(request, 'Capteurs.html')