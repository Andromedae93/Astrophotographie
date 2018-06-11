from django.conf.urls import url
from .views import AccueilTemplateView


urlpatterns = [
    url(r'^Accueil$', AccueilTemplateView.as_view(), name='Accueil'),
]