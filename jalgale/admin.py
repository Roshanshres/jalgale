from django.contrib import admin
from .models import Project
from .models import Sitesetting
from .models import Page
from .models import Testimonial
from .models import Album
from .models import Gallery

# Register your models here.

admin.site.register(Project)
admin.site.register(Sitesetting)
admin.site.register(Page)
admin.site.register(Testimonial)
admin.site.register(Album)
admin.site.register(Gallery)