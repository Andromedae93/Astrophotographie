from django.shortcuts import render, reverse, get_object_or_404, render_to_response


def AccueilMeteo(request):

    return render(request, 'AccueilMeteo.html')
