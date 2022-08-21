from django.contrib import admin
from .models import User,Userprofile,Post,Pokes,likes,Comments,Messages,PlogPost,PlogPostComments,Bussines,BussinesManager,BussinesStaff,Shift

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "email",
        
    )
admin.site.register(User, UserAdmin)
admin.site.register([Userprofile,Post,likes,Pokes,Comments,Messages,PlogPost,PlogPostComments,Bussines,BussinesManager,BussinesStaff,Shift])
