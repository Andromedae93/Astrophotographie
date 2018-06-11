from django.contrib import admin

from .models import Photo

class PhotoAdmin(admin.ModelAdmin) :

	fields = ["Nom", "Designation", "Type_objet", "Instrument", "Imageur", "Monture", "Instrument_Guidage", "Imageur_Guidage", "Reducteur", "Logiciels", 
    	"Date", "Nombre_Pose", "Temps_Pose", "Integration", "Darks", "Flats", "Bias", "Lunaison", "FWHM", "Temperature", "Lieu", "Image_upload"]

admin.site.register(Photo,PhotoAdmin)