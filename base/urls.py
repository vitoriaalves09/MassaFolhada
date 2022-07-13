from django.urls import path
from .views import HomeView


urlpatterns = [
    path('inicio/', HomeView.as_view(), name='inicio'),
    path('about/', AboutView.as_view()),
]