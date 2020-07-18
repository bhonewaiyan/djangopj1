from django.shortcuts import render

# Create your views here.
def bbq(request):
	return render(request, 'malaxiangou/bbq.html')
	