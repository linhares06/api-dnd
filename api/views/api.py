from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..models import Monster, Equipment
from ..serializers import MonsterSerializer, EquipmentSerializer


@api_view()
def monster_api_detail(request, name):
    monster = get_object_or_404(Monster, name=name)
    serializer = MonsterSerializer(
        instance=monster,
        context={'request': request},
    )
    return Response(serializer.data)

@api_view(['GET'])
def monster_api_list(request):
    monsters = Monster.objects.all()
    serializer = MonsterSerializer(
        monsters, 
        many=True,
    )
    return Response(serializer.data)

@api_view()
def equipment_api_detail(request, name):
    equipment = get_object_or_404(Equipment, name=name)
    serializer = EquipmentSerializer(
        instance=equipment,
        context={'request': request},
    )
    return Response(serializer.data)