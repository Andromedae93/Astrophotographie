from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^AccueilContact$', views.AccueilContact, name='AccueilContact'),
]