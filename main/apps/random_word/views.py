# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    if not request.session.values():
        request.session['count'] = 0

    return render(request, 'random_word/index.html')

def generate(request):
    if request.method == 'POST':
        context = {
            'word': get_random_string(1, allowed_chars='abcdefghijklmnopqrstuvwxyz') + get_random_string(2,allowed_chars='acdefghilmnoprstuy') + get_random_string(1,allowed_chars='abcdefghijklmnopqrstuvwxyz')
        }
        request.session['count'] += 1
        return render(request, 'random_word/index.html', context)
    else:
        return redirect('/')

def reset(request):
    request.session['count'] = 0
    return redirect('/')