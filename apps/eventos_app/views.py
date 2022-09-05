from django.shortcuts import render
from .models import Evento
from django.http.response import Http404

def proyectos(request):
    return render(request, 'proyectos.html')

def donar(request):
    return render(request, 'donar.html')

def eventos(request):
    lista_eventos = Evento.objects.all().order_by('-id')
    context = {
        "eventos": lista_eventos,
    }
    print()
    return render(request, 'eventos.html', context)


def eventDetail(request, id):
    try:
        evento = Evento.objects.get(id=id)
    except Evento.DoesNotExist:
        raise Http404('El Evento solicitado no existe')

    context = {
        "evento": evento,
    }
    return render(request, 'eventDetail.html', context)