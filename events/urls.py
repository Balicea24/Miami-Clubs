from django.contrib import admin
from django.urls import path
from events import views
clubs = ["Space", "Treehouse"]

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('Space/', views.clubs, name='clubs')
]
