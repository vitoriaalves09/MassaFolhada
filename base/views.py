#from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class HomeView(TemplateView):
    template_name = 'pages/home.html'
class LoginView(TemplateView):
    template_name = 'login.html'
class AboutView(TemplateView):
    template_name = 'about.html'
class MenuView(TemplateView):
    template_name = 'menu.html'
class InformationView(TemplateView):
    template_name = 'information.html'
class PaymentView(TemplateView):
    template_name = 'payment.html'
class TableView(TemplateView):
    template_name = 'table.html'
class ProcedureView(TemplateView):
    template_name = 'procedure.html'
class FinishingView(TemplateView):
    template_name = 'finishing.html'
class PersonalDataView(TemplateView):
    template_name = 'personalData.html'