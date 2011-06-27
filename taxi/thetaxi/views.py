# Create your views here.
from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect
from models import Taxi, Ratings
from django import forms
from django.forms import ModelForm, CharField
from django.views.decorators.csrf import csrf_exempt

class TaxiForm(ModelForm):
	class Meta:
		model =Ratings
		exclude=['created']
		#widgets = {'carnumber': CharField()}
	


@csrf_exempt
def add(request):
	
	if request.method == 'POST':
		form = TaxiForm(request.POST)
		return HttpResponseRedirect('/thetaxi/home')

	else:
		form =TaxiForm()
	t = loader.get_template('thetaxi/add.html')
	c = Context({'form':form.as_p()})
	return HttpResponse(t.render(c))



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
		rating = Ratings.objects.filter(carnumber = request.GET['search'])
		for i in rating:
			totalrate+=rating.rate
		totalrate/= len(rating)
		form = RatingsForm(request.GET,instance=taxi)
		return HttpResponseRedirect(request.path)
	else:
		form = RatingsForm()
	t = loader.get_template('/thetaxi/details.html')
		
	c = Context({'taxi':rating, 'form':form.as_p(), 'totalrate':totalrate, 'totalrate':totalrate})
	return HttpResponse(t.render(c))
 
