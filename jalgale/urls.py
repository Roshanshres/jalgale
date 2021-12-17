from django.urls import path
from django.urls.resolvers import URLPattern

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("projects", views.projects, name="projects"),
    path("project/<int:project_id>", views.project_detail, name="project_detail"),
    path("about-us", views.about_us, name="about_us")
]