from django.shortcuts import render
from django.http import HttpResponse
def data(request):
	l=[]
	context={
		'l':l

	}
	return render(request,'data.html',context)

# Create your views here.
