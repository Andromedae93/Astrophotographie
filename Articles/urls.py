from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^Articles', views.AccueilArticles, name='Articles'),
]