from django.contrib import admin

from tab.models import Post, Application


class PostAdmin(admin.ModelAdmin):
    list_display = ('subject', 'create_date')


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('studentnumber', 'name', 'phonenumber', 'create_date')


admin.site.register(Post, PostAdmin)
admin.site.register(Application, ApplicationAdmin)
