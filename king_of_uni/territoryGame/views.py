"""
Provides Views for territories, detail_territory
"""
from warnings import catch_warnings
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
from datetime import datetime, timedelta
from django.utils import timezone

__author__ = "Jakupov Dias, Edward Calonghi"

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
                    tooltip='Click for the name', popup=building.buildingInfo(),
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
                    tooltip='Click for the name', popup="Distance to " + building.name + " is " + str(distance) + "m",
                    icon=folium.Icon(color='red', icon='cloud')).add_to(map)
            #draw line between user and building
            line = folium.PolyLine(locations = [pointA, pointB], weight=2, clolor='red')
            map.add_child(line)
            if distance < 200:
                context['enable'] = True
                messages.success(request, 'You can capture the territory') 
            else:
                messages.error(request, 'You are too far from the territory') 
    map = map._repr_html_()

    if 'capture' in request.POST:
        form = CreateTerritoryCaptureForm(request.POST)
        # check the builidings capture date to see if it was recently captured if
        # the building has no cature date the check is bypassed
        try:
            elapesed_time = timezone.now() - building.capture_date
            cooldown = timedelta(hours=24)
        except:
            elapesed_time = 1
            cooldown = 0
        print(elapesed_time)
        print(cooldown)
        if elapesed_time > cooldown:
            if form.is_valid():
                obj = form.save(commit=False)
                username = Account.objects.filter(username = request.user.username).first()
                obj.team = username.belongs_to_group
                obj.territory_name = building
                obj.save()
                form = CreateTerritoryCaptureForm
                if str(building.holder) == str(user.belongs_to_group):
                    # saves data in the Building model
                    building.is_captured = True
                    building.holder = user.belongs_to_group.name
                    building.capture_date = datetime.now()
                    building.streak *= 2
                    building.save()
                    # adds points to user and saves data in Account model
                    user.score += 20
                    user.save()
                    # adds user points to teams points and saves data in Group Model
                    group = user.belongs_to_group
                    group.point_total += 10 * building.streak
                    group.save()                
                else:
                    # saves data in the Building model
                    building.is_captured = True
                    building.holder = user.belongs_to_group.name
                    building.capture_date = datetime.now()
                    building.streak = 1
                    building.save()
                    # adds points to user and saves data in Account model
                    user.score += 10
                    user.save()
                    # adds user points to teams points and saves data in Group Model
                    group = user.belongs_to_group
                    group.point_total += 10
                    group.save()
                return redirect('territory_game:territories')
        else:
            messages.error(request, 'Territory still on cooldown: '+str(cooldown - elapesed_time)+' left')
    else:
        form = CreateTerritoryCaptureForm()      
        
    context['form'] = form
    context['building'] = building
    context['map'] = map
    return render(request, 'territoryGame/detail_territory.html', context)
