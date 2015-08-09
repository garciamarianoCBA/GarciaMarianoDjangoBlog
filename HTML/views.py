from django.template import RequestContext
from django.shortcuts import render_to_response, render, redirect

# Create your views here.

def home(request):
    context = RequestContext(request)
    return render_to_response('mipagina.html',
                             context)
def cv(request):
    context = RequestContext(request)
    return render_to_response('CV.html',
                             context)
def recetas(request):
    context = RequestContext(request)
    return render_to_response('recetas.html',
                             context)
def programas(request):
    context = RequestContext(request)
    return render_to_response('PyU.html',
                             context)
def contacto(request):
    context = RequestContext(request)
    return render_to_response('contacto.html',
                             context)
def calc(request):
    context = RequestContext(request)
    return render_to_response('index.html',
                             context)
def comv(request):
    context = RequestContext(request)
    return render_to_response('comvertor.html',
                             context)
def cron(request):
    context = RequestContext(request)
    return render_to_response('cronometro.html',
                             context)
def imagen(request):
    context = RequestContext(request)
    return render_to_response('Image.html',
                             context)
def boton(request):
    context = RequestContext(request)
    return render_to_response('boton.html',
                             context)
            