from django.shortcuts import render
from account.models import Account
from gameKeeper.models import Building
import folium
# Create your views here.
def home_screen_view(request):
    context = {}
    buildings = Building.objects.all()
    map = folium.Map(location = [50.738099451637, -3.53507522602482], zoom_start = 15)
    for building in buildings:
        if building.is_active:
            folium.Marker(location = [building.latitude, building.longitude],
                        tooltip='Click for the name', popup=building.name).add_to(map)
    map = map._repr_html_()
    accounts = Account.objects.all()
    context['accounts'] = accounts
    context['map'] = map


    return render(request, "personal/home.html", context)