from django.shortcuts import render, reverse, get_object_or_404, render_to_response, HttpResponseRedirect

from .models import *
from .forms import *

def AccueilContact(request):
    # Fonction permettant de créer le formulaire livre d'or

    if request.method == 'POST':

        form = ContactForm(request.POST or None)

        if form.is_valid():  # Vérification sur la validité des données
            post = form.save()
            return HttpResponseRedirect(reverse('AccueilContact'))

    else:
        form = ContactForm()

    messages = Contact.objects.all().order_by("-date")

    context = {
        "form": form,
        "messages":messages,
    }

    return render(request, 'AccueilContact.html', context)
