from django.contrib import admin
from django.urls import path
from django.urls import re_path
from events import views

clubList = ["Space", "Treehouse", "ElectricPickle",
            "Story", "LIV", "E11even",
            "DoNotSitOnTheFurniture"]

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    re_path(r'^('+"|".join(clubList)+')/$', views.club, name='club')
]
