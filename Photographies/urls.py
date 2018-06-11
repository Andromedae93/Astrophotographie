from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^AccueilPhotographies$', views.AccueilPhotographies, name='AccueilPhotographies'),
    url(r'^Planetaire$', views.Planetaire, name='Planetaire'),
    url(r'^Galaxies$', views.Galaxies, name='Galaxies'),
    url(r'^Nebuleuses_Diffuses$', views.NebuleusesDiffuses, name='Nebuleuses_Diffuses'),
    url(r'^Nebuleuses_Planetaires$', views.NebuleusesPlanetaires, name='Nebuleuses_Planetaires'),
	url(r'^Amas_Globulaires$', views.AmasGlobulaires, name='Amas_Globulaires'),
	url(r'^Amas_Ouverts$', views.AmasOuverts, name='Amas_Ouverts'),
    url(r'^Autres$', views.Autres, name='Autres'),
] 