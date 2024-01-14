from django.contrib import admin
from django.contrib.auth.models import Group, User

from blog import models


@admin.register(models.Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "status", "created_at"]


# admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.site_header = "techTong Admin Panel"
admin.site.site_title = "techTong"
admin.site.index_title = "Administration"
