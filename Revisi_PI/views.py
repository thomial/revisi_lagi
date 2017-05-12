# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from . import LogicProgram
from forms import Document
from models import *

# Create your views here.

def home(request):

    return render (request, 'home/home.html', {})

def upload_file_csv(request):
    global url

    if request.method == 'POST':
        form = Document(request.POST, request.FILES)
        if form.is_valid():
            save = form.save()
            id = save.id
            setData = LogicProgram.Data(id)
            setData.ambil_data()
            setData.set_regresi_korelasi()
            url = reverse('home')
        return HttpResponseRedirect(url)
    else:
        form = Document()
    return render (request, 'home/upload_file_csv.html', {'form' : form})

