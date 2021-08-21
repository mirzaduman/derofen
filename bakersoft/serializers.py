from rest_framework import serializers
from .models import Produkt


class ProduktSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Produkt
        fields = ('id', 'name', 'getreide', 'gewicht', 'kalorien_100g', 'kalorien_gesamt', 'verfugbar')
