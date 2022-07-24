from django.contrib import admin
from django.forms import Textarea
from .models import *

# Register your models here.

# class ProjectAdmin(admin.ModelAdmin):
#     formfield_overrides = {
#         models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
#     }


admin.site.register(Author)
admin.site.register(Project)
