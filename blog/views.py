from django.shortcuts import render
from .models import News


# news = [
#     {
#     'title': 'Our first publications',
#     'text': 'Some text',
#     'date': '4.02.2022',
#     'author': 'admin',
#     'ref': 'N+1'
#      },
#     {
#     'title': 'Our second publications',
#     'text': 'Some text',
#     'date': '4.02.2022',
#     'author': 'Polina',
#     'ref': 'N+1'
#     }
#        ]

def home(request):
    data = {
        'news': News.objects.all(),
        'title': 'Главная страница блога'
    }
    return render(request, 'blog/home.html', data)


def contacts(request):
    return render(request, 'blog/contacts.html', {'title': "Страница про нас"})
