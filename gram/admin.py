from django.contrib import admin
from .models import Image , Profile , Comment , Follow

# class NewpostAdmin(admin.ModelAdmin):
#     filter_horizontal =('tags',)

admin.site.register(Image)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Follow)

#admin.site.register(Article)
#admin.site.register(tags)

# admin.site.register(Newpost,Admin)
# admin.site.register(tags)
