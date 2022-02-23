from django import forms
from django.shortcuts import render, redirect, get_object_or_404
from account.models import Account
from gameKeeper.models import Building
from territoryGame.models import TerritoryCapture
from territoryGame.forms import CreateTerritoryCaptureForm, UserLocationForm
from .utils import get_center_coordinates, get_zoom
from django.contrib import messages
import folium
from geopy.distance import geodesic
import decimal

# Create your views here.



def territories_view(request):
    context = {}

    if not request.user.is_authenticated:
        return redirect('login')

    buildings = Building.objects.all()

    context['buildings'] = buildings

    
    return render(request, 'territoryGame/territories.html', context)

def detail_territory_view(request, slug):

    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect('login')

    building = get_object_or_404(Building, slug=slug)

    #destindation coordinates

    building_latitude = building.latitude
    building_longitude = building.longitude

    #foliun map modificatiom
    map = folium.Map(location = get_center_coordinates(building_latitude, building_longitude), zoom_start = 15)
    
    #building marker
    folium.Marker(location = [building_latitude, building_longitude],
                    tooltip='Click for the name', popup=building.name,
                    icon=folium.Icon(color='blue',icon='info-sign')).add_to(map)
                    

    if 'showLocation' in request.POST:
        form = UserLocationForm(request.POST)
        if form.is_valid():
            latitude = request.POST['latitude']
            longitude = request.POST['longitude']
            user.latitude = latitude
            user.longitude = longitude
            user.save()
            #distance calculation
            pointA = (building_latitude,building_longitude)
            pointB = (latitude, longitude)
            distance = round(geodesic(pointA,pointB).meters)
            map = folium.Map(location = get_center_coordinates(building_latitude, building_longitude, decimal.Decimal(latitude), decimal.Decimal(longitude)), zoom_start = get_zoom(distance))
            #building marker
            folium.Marker(location = [building_latitude, building_longitude],
                    tooltip='Click for the name', popup=building.name,
                    icon=folium.Icon(color='blue',icon='info-sign')).add_to(map)
            #user marker
            folium.Marker(location = [latitude, longitude],
                    tooltip='Click for the name', popup="Distance to " + building.name + " is " + str(distance),
                    icon=folium.Icon(color='red', icon='cloud')).add_to(map)
            #draw line between user and building
            line = folium.PolyLine(locations = [pointA, pointB], weight=2, clolor='red')
            map.add_child(line)
            if distance < 200:
                messages.success(request, 'You can capture the territory') 
            else:
                messages.error(request, 'You are too far from the territory') 
    map = map._repr_html_()

    if 'capture' in request.POST:
        form = CreateTerritoryCaptureForm(request.POST)
        if not building.is_captured:
            if form.is_valid():
                building.is_captured = True
                building.save()
                obj = form.save(commit=False)
                username = Account.objects.filter(username = request.user.username).first()
                obj.username = username
                territory_name = building
                obj.territory_name = territory_name
                obj.save()
                form = CreateTerritoryCaptureForm
                return redirect('territory_game:territories')
    else:
        form = CreateTerritoryCaptureForm()      
        
    context['form'] = form
    context['building'] = building
    context['map'] = map
    return render(request, 'territoryGame/detail_territory.html', context)
