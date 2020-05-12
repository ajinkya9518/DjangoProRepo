from django.urls import path
from .views import *

urlpatterns = [
    path('news/',NewspaperList.as_view()),
    path('newsdetail/<int:pk>/',NewsPaperDetail.as_view()),

]
