# snippets/admin.py
from django.contrib import admin
from . models import Snippet
from . models import Category
from . models import Carousel
from . models import Service
from . models import Tags
from . models import Profile
from . models import Inquiry
from . models import Concept



class SnippetAdmin(admin.ModelAdmin):
    readonly_fields = ('highlighted',)



admin.site.register(Snippet, SnippetAdmin)


admin.site.register(Category)

admin.site.register(Carousel)

admin.site.register(Tags)

admin.site.register(Service)
admin.site.register(Profile)
admin.site.register(Inquiry)
admin.site.register(Concept)