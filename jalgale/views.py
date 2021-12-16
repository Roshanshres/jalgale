from django.shortcuts import render

from jalgale.models import Project



# Create your views here.

def index(request):
    projt = Project.objects.all()
      
    return render(request, "index.html", {'projt': projt})
    