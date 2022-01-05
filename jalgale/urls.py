from django.urls import path
from django.urls.resolvers import URLPattern

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("projects", views.projects, name="projects"),
    path("project/<int:project_id>", views.project_detail, name="project_detail"),
    path("page/<str:page_slug>", views.page_detail, name="pages"),
    path("about-us", views.about_us, name="about_us"),
    path("services", views.services, name="services"),
    path("contact-us", views.contact_us,name="contact_us"),
    path("register", views.register,name="register"),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)