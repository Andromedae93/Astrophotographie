from django.shortcuts import render


# Fonction(s) liées à l'accueil de la partie Astrophoto
def AccueilArticles(request):
    return render(request, 'AccueilArticles.html')
