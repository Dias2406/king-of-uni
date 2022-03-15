"""
Provides views for home page and rules
"""
from distutils.command.build import build
from django.shortcuts import render
from account.models import Account
from gameKeeper.models import Building
from group.models import Group
import folium

__author__ = "Jakupov Dias, Edward Calonghi"

# Create your views here.
def home_screen_view(request):
    context = {}
    buildings = Building.objects.all()
    #foliun map modificatiom
    map = folium.Map(location = [50.738099451637, -3.53507522602482], zoom_start = 16)
    for building in buildings:
        if building.is_active:
            if not building.is_captured:
                #not captured building marker
                folium.Marker(location = [building.latitude, building.longitude],
                            tooltip='Click for the name', popup=building.name + ' is not captured',
                            icon=folium.Icon(color='green',icon='info-sign')).add_to(map)
            else:
                #captured building marker
                group = Group.objects.filter(name = building.holder).first()
                folium.Marker(location = [building.latitude, building.longitude],
                tooltip='Click for the name', popup=building.name + ' is captured by "' + building.holder + '" team',
                icon=folium.Icon(color=group.color,icon='info-sign')).add_to(map)

    map = map._repr_html_()
    context['map'] = map
    return render(request, "personal/home.html", context)

def rules_screen_view(request):
    return render(request,"personal/rules.html")

def leaderboard_view(request):
    context = {}
    groups = Group.objects.all().order_by('-point_total')
    context['groups'] = groups
    return render(request, "personal/leaderboard.html", context)