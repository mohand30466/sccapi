from django.contrib import admin
from .models import User,Userprofile,Post,likes,Comments,Messages,PlogPost,PlogPostComments

class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "email",
    )
admin.site.register(User, UserAdmin)
admin.site.register([Userprofile,Post,likes,Comments,Messages,PlogPost,PlogPostComments])
