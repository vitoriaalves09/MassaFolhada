from django.urls import path
from .views import HomeView


urlpatterns = [
    path('start/', HomeView.as_view(), name='start'),
    path('login/', LoginView.as_view(), name='login')
    path('about/', AboutView.as_view(), name='about'),
    path('menu/', MenuView.as_view(), name='menu'),
    path('information/', InformationView.as_view(), name='information'),
    path('payment/', PaymentView.as_view(), name='payment'),
    path('table/', TableView.as_view(), name='table'),
    path('procedure/', ProcedureView(), name='procedure'),
    path('finishing/', FinishingView(), name='finishing'),
    path('personalData/', PersonalDataView(), name='personalData'),

]