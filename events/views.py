from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from .MiamiClubsEvents import getInfo

def index(request):
    SpaceNames = getInfo("Space")

    return TemplateResponse(request, 'eventshome.html')

def space(request):
    Space = getInfo("Space")

    return TemplateResponse(request, 'space.html',
                            {"Space": Space,})

def treehouse(request):
    Treehouse = getInfo("Treehouse")

    return TemplateResponse(request, 'treehouse.html',
                            {"Treehouse": Treehouse,})

def electricpickle(request):
    ElectricPickle = getInfo("ElectricPickle")

    return TemplateResponse(request, 'electricpickle.html',
                            {"ElectricPickle": ElectricPickle,})

def story(request):
    Story = getInfo("Story")

    return TemplateResponse(request, 'story.html',
                            {"Story": Story,})

def liv(request):
    LIV = getInfo("LIV")

    return TemplateResponse(request, 'liv.html',
                            {"LIV": LIV,})

def e11even(request):
    E11even = getInfo("E11even")

    return TemplateResponse(request, 'e11even.html',
                            {"E11even": E11even,})

def donotsitonthefurniture(request):
    DoNotSitOnTheFurniture = getInfo("DoNotSitOnTheFurniture")

    return TemplateResponse(request, 'donotsitonthefurniture.html',
                            {"DoNotSitOnTheFurniture": DoNotSitOnTheFurniture,})
