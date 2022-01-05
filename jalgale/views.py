from django.core.checks import messages
from django.http.response import BadHeaderError, HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth

from django.core.mail import send_mail, BadHeaderError

from django.core.cache import cache

from jalgale.models import Project
from jalgale.models import ContactUs
from jalgale.models import Sitesetting
from jalgale.models import Page



# Create your views here.

def index(request):
    projects = Project.objects.all()

    setting = cache.get('siteSetting', None)
    if setting is None:
        siteSettings = Sitesetting.objects.all()[:1].get()
        cache.add('siteSetting', siteSettings)

    return render(request, "index.html", {'projects': projects, 'siteSettings': cache.get('siteSetting')})

def content_desc(request):
    pass

def projects(request):
    projects = Project.objects.all()
    page = Page.objects.get(slug='projects')
    return render(request, "projects.html", {'projects': projects, 'page': page, 'siteSettings': cache.get('siteSetting')})

def project_detail(request, project_id):
    project = Project.objects.get(id=project_id)
    return render(request, "project_detail.html", {'project': project, 'siteSettings': cache.get('siteSetting')})

def page_detail(request, page_slug):
    page = Page.objects.get(slug=page_slug)
    return render(request, "page_detail.html", {'page': page, 'siteSettings': cache.get('siteSetting')})

def about_us(request):
    return render(request, "about_us.html", {'siteSettings': cache.get('siteSetting')})

def services(request):
    return render(request, "services.html", {'siteSettings': cache.get('siteSetting')})

def contact_us(request):
    if request.method == 'POST':
        name =request.POST['name']
        email =request.POST['email']
        messages = request.POST['message']

        save_messages = ContactUs.objects.create(name=name, email=email, message=messages);
        # save_messages.save();
        print('message sent');
        return render(request,"contact_us.html")
        
    else:
        return render(request,"contact_us.html", {'siteSettings': cache.get('siteSetting')})
    
def contact(request):
    if request.method =='POST':
        form = contact_us(request.POST)
        if form.is_valid():
            subject ="Website Inquery"
            body = {
                'name': form.cleaned_data['name'],
                'email': form.cleand_data['email_address'],
                'message' : form.cleaned_data ['messages']
            }
            messages = "\n".join(body.values())

            try:
                send_mail(subject, messages,'admin@Jalgalenirman.com', ['admin@Jalgalenirman.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect ("index:homepage")
    
    form = contact_us()
    return render(request, ",index/contact_us.html", {'form': form})


def register(request):
    return render(request,"register.html", {'siteSettings': cache.get('siteSetting')})