from django.urls import path
from .views import *

urlpatterns = [
    path('main/', MainListCreateView.as_view()),
    path('title/', TitleListCreateView.as_view()),
    path('title/<int:pk>/', TitleDetailView.as_view()),
    path('card/', CardListCreateView.as_view()),
    path('card/<int:pk>/', CardDetailView.as_view()),
]