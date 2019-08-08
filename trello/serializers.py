from rest_framework import serializers
from .models import Title, Card, Comments, Backgroundcolor


# 리스트 관련 serializer
class TitleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = "__all__"


# 리스트 디테일 관련 serializer
class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = ['title', 'listSort']


# 코멘트 관련 serializer
class CommentsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'


# 코멘트 디테일 관련 serializer
class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['comment']


# 카드 관련 serializer
class CardListSerializer(serializers.ModelSerializer):
    comments = CommentsListSerializer(many=True)

    class Meta:
        model = Card
        fields = ['title', 'id', 'cardTitle', 'description', 'comments', 'cardSort']
        read_only_fields = ['description', 'comments']


# 카드 디테일 관련 serializer
class CardSerializer(serializers.ModelSerializer):
    comments = CommentsListSerializer(many=True)

    class Meta:
        model = Card
        fields = ['title', 'cardTitle', 'description', 'comments', 'cardSort']


# 트렐로 배경 화면 관련 serializer
class BackgroundcolorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Backgroundcolor
        fields = "__all__"


# 트렐로 메인 관련 serializer
class MainListSerializer(serializers.ModelSerializer):
    # cards = serializers.StringRelatedField(many=True)
    cards = CardListSerializer(many=True, read_only=True)

    class Meta:
        model = Title
        fields = ['id', 'title', 'listSort', 'cards']
