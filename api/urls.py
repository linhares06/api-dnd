from django.urls import path

from api import views

app_name = 'api'

urlpatterns = [
    path(
        'api/monster/<str:name>/',
        views.monster_api_detail,
        name='api_monster',
    ),
    path(
        'api/monsters',
        views.monster_api_list,
        name='api_monsters',
    ),
    path(
        'api/equipment/<str:name>/',
        views.equipment_api_detail,
        name='api_equipment',
    ),
]