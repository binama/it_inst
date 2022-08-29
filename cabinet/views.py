from django.shortcuts import render
from .models import Author


def get_cabinet(request):
    authors = Author.objects.all()
    print(locals())
    return render(request, 'cabinet.html', locals())