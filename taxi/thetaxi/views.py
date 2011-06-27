# Create your views here.
class RatingsForm(ModelForm):
	class Meta:
		model = Ratings
		exclude=['created', 'carnumber']

def taxi_details(request):
	taxi = Taxi.objects.get(carnumber = request.GET['search'])
	if request.method == 'GET':
		rating = Ratings(carnumber=taxi)
		form = RatingsForm(request.POST,instance=rating)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(request.path)
	else:
		form = RatingsForm()
	
	t = loader.get_template('thetaxi/detail.html')
	rating = Ratings.objects.filter(carnumber__pk=id)	
	c = Context({'taxi':Taxi, 'comments':comments, 'form':form.as_p()})
	return HttpResponse(t.render(c))
