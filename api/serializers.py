from rest_framework import serializers
from .models import Monster, Equipment

class MonsterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monster
        fields = [
            'name',
            'alignment',
            'hit_points',
        ]

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = [
            'name',
        ]