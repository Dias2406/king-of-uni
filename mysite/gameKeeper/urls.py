from django.urls import path

from gameKeeper.views import (
    create_building_view,
    detail_building_view,
    game_keeper_view,
)

from group.views import (
    groups_list_view,
    create_group_view,
)

app_name = 'game_keeper'

urlpatterns = [
    path('create_group/', create_group_view, name="create_group"),
    path('group/', groups_list_view, name="groups_list"),
    path('settings/', game_keeper_view, name="settings"),
    path('create/', create_building_view, name="create"),
    path('<slug>/', detail_building_view, name="detail"),
]