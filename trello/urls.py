from django.urls import path
from .views import *

urlpatterns = [
    # trello main 경로(모든 정보)
    path('main/', MainListView.as_view()),

    # trello list 관련 경로
    path('title/', TitleListCreateView.as_view()),
    path('title/<int:pk>/', TitleDetailView.as_view()),

    # trello card 관련 경로
    path('card/', CardListCreateView.as_view()),
    path('card/<int:pk>/', CardDetailView.as_view()),

    # trello card comment 관련 경로
    path('comments/', CommentsListCreateView.as_view()),
    path('comments/<int:pk>/', CommentsDetailView.as_view()),

    # trello backgroundcolor 관련 경로
    path('backgroundcolors/<int:pk>', BackgroundcolorDetailView.as_view()),
]