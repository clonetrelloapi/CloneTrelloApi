from rest_framework import serializers
from .models import List, Card

class ListOfListSerializer(serializers.ModelSerializer):
    cards = serializers.StringRelatedField(many=True)
    class Meta:
        model = List
        fields = ['id', 'name', 'cards']

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = ['name']

class CardListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['title']