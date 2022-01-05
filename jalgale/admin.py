from django.contrib import admin
from .models import Project
from .models import Sitesetting
from .models import Page

# Register your models here.

admin.site.register(Project)
admin.site.register(Sitesetting)
admin.site.register(Page)