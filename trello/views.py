from django.shortcuts import render
from .serializers import *
from .models import List, Card
from rest_framework import generics
from rest_framework.renderers import JSONRenderer

class ListOfListCreateView(generics.ListCreateAPIView):
    renderer_classes = [JSONRenderer]
    queryset = List.objects.all()
    serializer_class = ListOfListSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

class ListDetailView(generics.RetrieveUpdateDestroyAPIView):
    renderer_classes = [JSONRenderer]
    queryset = List.objects.all()
    serializer_class = ListSerializer

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
