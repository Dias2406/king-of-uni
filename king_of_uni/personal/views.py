from distutils.command.build import build
from django.shortcuts import render
from account.models import Account
from gameKeeper.models import Building
import folium
# Create your views here.
def home_screen_view(request):
    context = {}
    buildings = Building.objects.all()
    map = folium.Map(location = [50.738099451637, -3.53507522602482], zoom_start = 16)
    for building in buildings:
        if building.is_active:
            if not building.is_captured:
                folium.Marker(location = [building.latitude, building.longitude],
                            tooltip='Click for the name', popup=building.name + ' is not captured',
                            icon=folium.Icon(color='green',icon='info-sign')).add_to(map)
            else:
                folium.Marker(location = [building.latitude, building.longitude],
                tooltip='Click for the name', popup=building.name + ' is captured by ' + building.holder,
                icon=folium.Icon(color='red',icon='info-sign')).add_to(map)

    map = map._repr_html_()
    accounts = Account.objects.all().order_by('-score')
    context['accounts'] = accounts
    context['map'] = map


    return render(request, "personal/home.html", context)

def rules_screen_view(request):
    return render(request,"personal/rules.html")