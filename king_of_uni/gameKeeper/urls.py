from django.urls import path

from gameKeeper.views import (
    create_building_view,
    detail_building_view,
    game_keeper_view
)

app_name = 'game_keeper'

urlpatterns = [
    path('settings/', game_keeper_view, name="settings"),
    path('create/', create_building_view, name="create"),
    path('<slug>/', detail_building_view, name="detail"),
]