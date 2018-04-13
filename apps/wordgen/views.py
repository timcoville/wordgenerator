from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string


def index(request):
    if 'count' not in request.session:
        request.session['count'] = 1
    if 'word' not in request.session:
        word = get_random_string(length=14)
        request.session['word'] = word.upper()
    context = {
        "count": request.session['count'],
        "word": request.session['word']
    }
    return render (request, "wordgen/index.html", context)

def random_word(request):
    request.session['count'] += 1
    word = get_random_string(length=14)
    request.session['word'] = word.upper()
    return redirect ("/")