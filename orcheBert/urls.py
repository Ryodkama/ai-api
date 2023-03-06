from django.urls import path, include
from .views import GetHummingMIDI, GetHummingMIDIRandom, GetMyOrche

urlpatterns = [
    # path('<int:pk>/', DetailTodo.as_view()),
    path('', GetHummingMIDI.as_view()),
    path('getrnd', GetHummingMIDIRandom.as_view()),
    path('getmy', GetMyOrche.as_view()),
]