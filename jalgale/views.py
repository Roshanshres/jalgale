from django.shortcuts import render

from jalgale.models import Project



# Create your views here.

def index(request):
    projects = Project.objects.all()
    return render(request, "index.html", {'projects': projects})

def projects(request):
    projects = Project.objects.all()
    return render(request, "projects.html", {'projects': projects})

def project_detail(request, project_id):
    project = Project.objects.get(id=project_id)
    return render(request, "project_detail.html", {'project': project})

def about_us(request):
    return render(request, "about_us.html")
    