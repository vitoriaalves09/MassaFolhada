from django.urls import path
from .views import HomeView, LoginView, AboutView, MenuView, InformationView, PaymentView, TableView, ProcedureView, FinishingView, PersonalDataView 

urlpatterns = [
    path('start/', HomeView.as_view(), name='start'),
    path('login/', LoginView.as_view(), name='login'),
    path('about/', AboutView.as_view(), name='about'),
    path('menu/', MenuView.as_view(), name='menu'),
    path('information/', InformationView.as_view(), name='information'),
    path('payment/', PaymentView.as_view(), name='payment'),
    path('table/', TableView.as_view(), name='table'),
    path('procedure/', ProcedureView.as_view(), name='procedure'),
    path('finishing/', FinishingView.as_view(), name='finishing'),
    path('personalData/', PersonalDataView.as_view(), name='personalData'),

]