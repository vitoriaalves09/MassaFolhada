from django.shortcuts import render
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

def register(request):
    if request.method == 'GET':
        return render(request, "pages/register.html")
    
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = User.objects.filter(username = username).first()   
        if user:
            return render(request, "pages/permission.html")
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return render(request, "pages/home.html")