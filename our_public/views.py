from django.shortcuts import render
from .models import Public


def our_publication(request):
    data = {
        'Pub': Public.objects.all(),
        'title': 'Соль земли'
    }
    return render(request, 'our_public/home.html', data)
