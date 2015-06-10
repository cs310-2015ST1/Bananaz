from django.shortcuts import render
from django.template.loader import render_to_string
from .models import Garden

# Create your views here.
def index(request):
	gardens = Garden.objects.order_by('name')
	return render(request,'garden/index.html',
			{'gardens' : gardens})
