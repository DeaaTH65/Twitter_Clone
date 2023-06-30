from django.contrib import admin
from django.contrib.auth.models import Group, User


# Unregistering gropus and user in Admin section
admin.site.unregister(Group)
admin.site.unregister(User)



class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username"]
    

admin.site.register(User, UserAdmin)