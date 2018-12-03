from django.contrib import admin
from django.urls import path
from events import views
clubs = ["Space", "Treehouse"]

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('Space/', views.space, name='space'),
    path('Treehouse/', views.treehouse, name='treehouse'),
    path('ElectricPickle/', views.electricpickle, name='electricpickle'),
    path('Story/', views.story, name='story'),
    path('LIV/', views.liv, name='liv'),
    path('E11even/', views.e11even, name='e11even'),
    path('DoNotSitOnTheFurniture/', views.donotsitonthefurniture, name='donotsitonthefurniture')
]
