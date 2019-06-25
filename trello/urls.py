from django.urls import path
from .views import *

urlpatterns = [
    path('list/', ListOfListCreateView.as_view()),
    path('list/<int:pk>/', ListDetailView.as_view()),
    path('card/', CardListCreateView.as_view()),
    path('card/<int:pk>/', CardDetailView.as_view()),
]