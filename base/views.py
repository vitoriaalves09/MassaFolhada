#from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

'''
def home(request):
    return render(request. 'home.html')
'''
class HomeView(templateView):
    template_name = 'home.html'
class LoginView(templateView):
    template_name = 'login.html'
class AboutView(templateView):
    template_name = 'about.html'
class MenuView(templateView):
    template_name = 'menu.html'
class InformationView(templateView):
    template_name = 'information.html'
class PaymentView(templateView):
    template_name = 'payment.html'
class TableView(templateView):
    template_name = 'table.html'
class ProcedureView(templateView):
    template_name = 'procedure.html'
class FinishingView(templateView):
    template_name = 'finishing.html'
class PersonalDataView(templateView):
    template_name = 'personalData.html'