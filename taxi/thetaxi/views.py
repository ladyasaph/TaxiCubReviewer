# Create your views here.
from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect
from models import Taxi, Ratings
from django import forms
from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt

class SearchForm(forms.Form):
	search = forms.TextField()

def home(request,):	 
	if request.method == 'POST':
		form = SearchForm(request.POST)
	else:
		form = SearchForm()
	
	

