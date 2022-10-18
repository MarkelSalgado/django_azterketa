from django.shortcuts import render
from django.urls import reverse

from .models import Kotxeak
from django.template import loader
from django.http import HttpResponse
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    kotxeak = Kotxeak.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'kotxeak': kotxeak,
    }
    return HttpResponse(template.render(context, request))


def cars(request):
    kotxeak = Kotxeak.objects.all()
    return render(request, 'our_cars.html', {'kotxeak': kotxeak})


def update(request, id):
    kotxe = Kotxeak.objects.get(id=id)
    template = loader.get_template('update_cars.html')
    context = {
        'kotxe': kotxe,
    }
    return HttpResponse(template.render(context, request))


def updaterecord(request):
    pre = request.POST['prezio']
    ida = request.POST['ida']
    kotxe = Kotxeak.objects.get(id=ida)
    kotxe.alokatzeko_prezioa = pre
    kotxe.save()
    return HttpResponseRedirect(reverse('cars'))


def delete(request, id):
    kotxe = Kotxeak.objects.get(id=id)
    kotxe.delete()
    return HttpResponseRedirect(reverse('cars'))


def autoak_gehitu(request):
    kotxeak = Kotxeak.objects.all()
    return render(request, 'add_car.html', {'kotxeak': kotxeak})


def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))


def addrecord(request):
    x = request.POST['kt_matrikula']
    y = request.POST['kt_marka']
    z = request.POST['kt_modeloa']
    i = request.POST['kt_kolorea']
    j = request.POST['kt_aloka_prezio']

    kotxe = Kotxeak(matrikula=x, marka=y, modeloa=z, kolorea=i, alokatzeko_prezioa=j)
    kotxe.save()
    return HttpResponseRedirect(reverse('autoak_gehitu'))
