from django.shortcuts import render
from .serializers import *
from .models import Title, Card
from rest_framework import generics
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

class MainListView(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Title.objects.all()
    serializer_class = MainListSerializer

class TitleListCreateView(generics.ListCreateAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Title.objects.all()
    serializer_class = MainListSerializer

    # def create(self, request, *args, **kwargs):
    #     return super().create(request, *args, **kwargs)

    # def create(self, request, *args, **kwargs):
    #     return super().create(request, *args, **kwargs)

class TitleDetailView(generics.RetrieveUpdateDestroyAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Title.objects.all()
    serializer_class = TitleSerializer

class CardListCreateView(generics.ListCreateAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Card.objects.all()
    serializer_class = MainListSerializer

    # def create(self, request, *args, **kwargs):
    #     return super().create(request, *args, **kwargs)

class CardDetailView(generics.RetrieveUpdateDestroyAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Card.objects.all()
    serializer_class = CardSerializer

class CommentsListCreateView(generics.ListCreateAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Comments.objects.all()
    serializer_class = CommentsListSerializer

class CommentsDetailView(generics.RetrieveUpdateDestroyAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer


class BackgroundcolorDetailView(generics.RetrieveUpdateAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Backgroundcolor.objects.all()
    serializer_class = BackgroundcolorSerializer

