# Create your views here.
from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect
from models import Taxi, Ratings
from django import forms
from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt

class SearchForm(forms.Form):
	search = forms.CharField()

def home(request):	 
	if request.method == 'POST':
		form = SearchForm(request.POST)

	form = SearchForm()
 	t = loader.get_template('thetaxi/home.html')	
	c = Context({'form':form.as_p()})
	return HttpResponse(t.render(c))
	
class RatingsForm(ModelForm):
	class Meta:
		model = Ratings
		exclude=['created', 'carnumber']

def taxi_details(request):

	if request.method == 'GET':
		taxi = Taxi.objects.get(carnumber = request.GET['search'])
		form = RatingsForm(request.GET,instance=rating)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(request.path)
	else:
		form = RatingsForm()
	
	t = loader.get_template('thetaxi/detail.html')
	rating = Ratings.objects.filter(carnumber__pk=id)	
	c = Context({'taxi':Taxi, 'comments':comments, 'form':form.as_p()})
	return HttpResponse(t.render(c))
