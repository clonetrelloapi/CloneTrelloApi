from django.shortcuts import render
from .serializers import *
from .models import Title, Card
from rest_framework import generics
from rest_framework.renderers import JSONRenderer


class MainListCreateView(generics.ListCreateAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Title.objects.all()
    serializer_class = MainListSerializer


class TitleListCreateView(generics.ListCreateAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Title.objects.all()
    serializer_class = TitleListSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class TitleDetailView(generics.RetrieveUpdateDestroyAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Title.objects.all()
    serializer_class = TitleSerializer

class CardListCreateView(generics.ListCreateAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Card.objects.all()
    serializer_class = CardListSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

class CardDetailView(generics.RetrieveUpdateDestroyAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Card.objects.all()
    serializer_class = CardSerializer
