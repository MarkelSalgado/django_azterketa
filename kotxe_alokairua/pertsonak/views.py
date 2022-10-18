from django.shortcuts import render

from django.template import loader
from django.http import HttpResponse
from django.db import models
from django.urls import reverse

from django.template import loader
from django.http import HttpResponseRedirect
from .models import Pertsonak


# Create your views here.
def pertsonak_index(request):
    pertsonak = Pertsonak.objects.all().values()
    template = loader.get_template('pertsonak_index.html')
    context = {
        'pertsonak': pertsonak,
    }
    return HttpResponse(template.render(context, request))

def pertsonak_gehitu(request):
    pertsonak = Pertsonak.objects.all()
    return render(request, 'add_person.html', {'pertsonak': pertsonak})


def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))


def addrecord(request):
    x = request.POST['pert_izena']
    y = request.POST['pert_abizena']
    z = request.POST['pert_dni']
    i = request.POST['perts_aloka']

    pertsona = Pertsonak(izena=x, abizena=y, dni=z, alokagai_daukan_kotxearen_id=i)
    pertsona.save()
    return HttpResponseRedirect(reverse('pertsonak_gehitu'))