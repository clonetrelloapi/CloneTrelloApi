from rest_framework import serializers
from .models import Title, Card

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

class MainListSerializer(serializers.ModelSerializer):
    # cards = serializers.StringRelatedField(many=True)
    cards = CardListSerializer(many=True, read_only=True)

    class Meta:
        model = Title
        fields = ['id', 'title', 'cards']