from __future__ import unicode_literals

from django.db import models

TYPE_CHOICES = (
    ('Galaxie', 'Galaxie'),
    ('Nébuleuse Diffuse', u'Nébuleuse Diffuse'),
    ('Nébuleuse Planétaire',u'Nébuleuse Planétaire'),
    ('Amas Globulaire',u'Amas Globulaire'),
    ('Amas Ouvert','Amas Ouvert'),
)

class Photo(models.Model) :

	Nom					= models.CharField(max_length=50, verbose_name="Nom de l'objet", blank=False)
	Designation 		= models.CharField(max_length=50, verbose_name="Désignation de l'objet", blank=False, default="NGC ")
	Type_objet 			= models.CharField(max_length=50,choices=TYPE_CHOICES, verbose_name="Type d'objet")
	Instrument 	 		= models.CharField(max_length=50, verbose_name="Instrument", blank=False)
	Imageur 			= models.CharField(max_length=50, verbose_name="Imageur", blank=False)
	Monture 			= models.CharField(max_length=50, verbose_name="Monture", blank=False)
	Instrument_Guidage  = models.CharField(max_length=50, verbose_name="Instrument de Guidage", blank=False)
	Imageur_Guidage		= models.CharField(max_length=50, verbose_name="Imageur de Guidage", blank=False)
	Reducteur			= models.CharField(max_length=50, verbose_name="Reducteur/Correcteur de Focale", blank=False)
	Logiciels			= models.CharField(max_length=60, verbose_name="Logiciels", blank=False)
	Date 				= models.DateField()
	Nombre_Pose			= models.IntegerField(verbose_name="Nombre de pose total")
	Temps_Pose			= models.IntegerField(verbose_name="Temps de pose unitaire")
	Integration			= models.FloatField(verbose_name="Temps de pose total")
	Darks				= models.IntegerField(verbose_name="Nombre de Darks")
	Flats				= models.IntegerField(verbose_name="Nombre de Flats")
	Bias				= models.IntegerField(verbose_name="Nombre de Bias")
	Lunaison			= models.FloatField(verbose_name="Pourcentage de Lune")
	FWHM				= models.FloatField(verbose_name="FWHM moyenne")
	Temperature			= models.IntegerField(verbose_name="Température")
	Lieu 				= models.CharField(max_length=60, verbose_name="Lieu de Photo", blank=False)
	Image_upload		= models.ImageField(upload_to='Media/', width_field=None, height_field=None, verbose_name="Image")

	def __str__(self):
   		return self.Designation

	def __unicode__(self):
		return unicode (self.id, self.Nom, self.Designation, self.Type_objet, self.Instrument, self.Imageur, self.Monture, self.Instrument_Guidage, self.Imageur_Guidage, self.Reducteur, self.Logiciels, 
    	self.Date, self.Nombre_Pose, self.Temps_Pose, self.Integration, self.Darks, self.Flats, self.Bias, self.Lunaison, self.FWHM, self.Temperature, self.Lieu, self.Image_upload)