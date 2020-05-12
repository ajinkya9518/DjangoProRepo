from django.urls import  path
from secapp.views import *
urlpatterns = [
    path('home/', home),
    path('state/', stateadd),
    path('update/<int:id>/',update),
    path('updatestate/<int:id>/',updatestate),
    path('deletestate/<int:id>/',deletestate),

]
