from django.shortcuts import render, reverse, get_object_or_404, render_to_response

#from Photographies.models import Photo


def AccueilPresentation(request):

    return render(request, 'AccueilPresentation.html')