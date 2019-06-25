from rest_framework import serializers
from .models import Title, Card

class MainListSerializer(serializers.ModelSerializer):
    cards = serializers.StringRelatedField(many=True)

    class Meta:
        model = Title
        fields = ['id', 'title', 'cards']

class TitleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = "__all__"

class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = ['title']

class CardListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['title']