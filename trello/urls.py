from django.urls import path
from .views import *

urlpatterns = [
    path('main/', MainListView.as_view()),

    path('title/', TitleListCreateView.as_view()),
    path('title/<int:pk>/', TitleDetailView.as_view()),

    path('card/', CardListCreateView.as_view()),
    path('card/<int:pk>/', CardDetailView.as_view()),

    path('comments/', CommentsListCreateView.as_view()),
    path('comments/<int:pk>/', CommentsDetailView.as_view()),

    path('backgroundcolors/<int:pk>', BackgroundcolorDetailView.as_view()),
]