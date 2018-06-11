from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^AccueilPresentation$', views.AccueilPresentation, name='AccueilPresentation'),
]