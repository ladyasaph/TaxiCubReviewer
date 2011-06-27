class TaxiForm(ModelForm):
	class Meta:
		model =Ratings
		exclude=['created']
	


@csrf_exempt
def add(request):
	
	if request.method == 'POST':
		form = TaxiForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(request.path)
	else:
		form =TaxiForm()
	t = loader.get_template('thetaxi/add.html')
	c = Context({'form':form.as_p()})
	return HttpResponse(t.render(c))	
