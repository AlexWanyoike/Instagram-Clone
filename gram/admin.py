from django.contrib import admin
from .models import Newpost,tags

class NewpostAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)

admin.site.register(Newpost)
#admin.site.register(Article)
admin.site.register(tags)

# admin.site.register(Newpost,Admin)
# admin.site.register(tags)
