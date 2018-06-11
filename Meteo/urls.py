from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^AccueilMeteo$', views.AccueilMeteo, name='AccueilMeteo'),
]