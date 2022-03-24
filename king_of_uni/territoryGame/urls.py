from django.urls import path

from territoryGame.views import (
    territories_view,
    detail_territory_view,
)

app_name = 'territory_game'

urlpatterns = [
    path('', territories_view, name="territories"),
    path('<slug>/', detail_territory_view, name="detail_territory"),
]