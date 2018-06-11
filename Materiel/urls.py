from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^Accueil$', views.Accueil, name='AccueilMateriel'),
    url(r'^Optiques$', views.Optiques, name='Optiques'),
    url(r'^Monture$', views.Monture, name='Monture'),
    url(r'^Capteurs$', views.Capteurs, name='Capteurs'),
]