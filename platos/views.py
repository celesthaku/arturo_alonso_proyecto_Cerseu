from django.shortcuts import render

from platos.models import Platos


# Create your views here.


def platos(request):
    p = Platos(nombre='seco a la norteña', precio=25, procedencia='Peru')
    r = Platos(nombre='arroz con pollo', precio=40, procedencia='Peru')
    s = Platos(nombre='frejoles', precio=30, procedencia='Peru')
    p.save()
    r.save()
    s.save()

    data_context = Platos.objects.filter(precio__gte=40)


    return render(request, 'platos/platos.html', context= {'data' : data_context})