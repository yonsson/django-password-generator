from django.shortcuts import render
from django.http import HttpResponse
import random
import string


# Create your views here.
def home(request):
    return render(request, 'generator/home.html')


def password(request):

    characters = list(string.ascii_lowercase)

    if request.GET.get('uppercase'):
        characters.extend(list(string.ascii_uppercase))
    if request.GET.get('special'):
        characters.extend(list(string.punctuation))
    if request.GET.get('numbers'):
        characters.extend([str(i) for i in range(10)])

    length = int(request.GET.get('length', 12))
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password':thepassword})


def description(request):
    return render(request, 'generator/description.html')