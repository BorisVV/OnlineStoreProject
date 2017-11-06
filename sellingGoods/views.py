from django.shortcuts import render

# View for the home page

def home(request):
	return render(request, 'home/index.html')
