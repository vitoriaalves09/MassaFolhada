#from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class HomeView(TemplateView):
    template_name = 'pages/home.html'
class LoginView(TemplateView):
    template_name = 'pages/login.html'
class AboutView(TemplateView):
    template_name = 'pages/about.html'
class MenuView(TemplateView):
    template_name = 'pages/menu.html'
class InformationView(TemplateView):
    template_name = 'pages/information.html'
class PaymentView(TemplateView):
    template_name = 'pages/payment.html'
class TableView(TemplateView):
    template_name = 'pages/table.html'
class ProcedureView(TemplateView):
    template_name = 'pages/procedure.html'
class FinishingView(TemplateView):
    template_name = 'pages/finishing.html'
class PersonalDataView(TemplateView):
    template_name = 'pages/personalData.html'