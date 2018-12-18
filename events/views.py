from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from .MiamiClubsEvents import getInfo

def club(request, club):
    clubName = club
    events = getInfo(str(club))

    return TemplateResponse(request, 'events.html',
                            {"events": events,
                            "clubName": clubName,})

def index(request):
    return TemplateResponse(request, 'eventshome.html')
