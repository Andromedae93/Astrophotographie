from django.db import models
from django.utils import timezone

class Contact(models.Model):
    nom             =           models.CharField(max_length=50, verbose_name="Nom", blank=False)
    prenom          =           models.CharField(max_length=50, verbose_name="Prenom", blank=False)
    description     =           models.CharField(max_length=450, verbose_name="Message", blank=False)
    date            =           models.DateField(default=timezone.now())

    @property
    def __unicode__(self):
        return unicode(self.id, self.nom, self.prenom, self.description)
