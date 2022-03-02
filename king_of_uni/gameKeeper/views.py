"""
Provides Views for game_keeper, create_building, detail_building
"""
from django.shortcuts import render, redirect, get_object_or_404
from gameKeeper.models import Building
from gameKeeper.forms import CreateBuildingForm
import folium

__author__ = "Jakupov Dias, Rob Campbell"

def game_keeper_view(request):
    context = {}

    if not request.user.is_authenticated:
        return redirect('login')

    buildings = Building.objects.all()

    context['buildings'] = buildings

    
    return render(request, 'game_keeper/settings.html', context)

def create_building_view(request):

    context = {}

    user = request.user
    if not user.is_authenticated:
        return redirect('login')
    form = CreateBuildingForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = CreateBuildingForm()
        return redirect('settings')
    context['form'] = form
    return render(request, 'game_keeper/create_building.html', context)

def detail_building_view(request, slug):
    context = {}

    building = get_object_or_404(Building, slug=slug)
    #foliun map modificatiom
    map = folium.Map(location = [50.738099451637, -3.53507522602482], zoom_start = 15)
    #building marker
    folium.Marker(location = [building.latitude, building.longitude],
                    tooltip='Click for the name', popup=building.name).add_to(map)

    map = map._repr_html_()
    #activating building
    if 'activate' in request.POST:
        building.is_active = True
        building.save()
        return redirect('game_keeper:settings')
    #deactivating building
    if 'deactivate' in request.POST:
        building.is_active = False
        building.save()
        return redirect('game_keeper:settings')
    context['building'] = building
    context['map'] = map
    return render(request, 'game_keeper/detail_building.html', context)
