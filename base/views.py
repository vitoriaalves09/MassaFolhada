#from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

'''
def home(request):
    return render('home.html')
'''
class HomeView(templateView):
    template_name = 'home.html'