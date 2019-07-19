from rest_framework import serializers
from .models import Title, Card, Comments, Backgroundcolor

class TitleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = "__all__"

class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = ['title', 'listSort']

class CommentsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['comment']

class CardListSerializer(serializers.ModelSerializer):
    comments = CommentsListSerializer(many=True, read_only=True)

    class Meta:
        model = Card
        fields = ['title', 'id', 'cardTitle', 'description', 'comments', 'cardSort']
        read_only_fields = ['description']


class CardSerializer(serializers.ModelSerializer):
    comments = CommentsListSerializer(many=True)

    class Meta:
        model = Card
        fields = ['title', 'cardTitle', 'description', 'comments', 'cardSort']


class BackgroundcolorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Backgroundcolor
        fields = "__all__"


class MainListSerializer(serializers.ModelSerializer):
    # cards = serializers.StringRelatedField(many=True)
    cards = CardListSerializer(many=True, read_only=True)

    class Meta:
        model = Title
        fields = ['id', 'title', 'listSort', 'cards']