from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile


# Unregistering gropus and user in Admin section
admin.site.unregister(Group)
admin.site.unregister(User)


class ProfileInLine(admin.StackedInline):
    model = Profile


class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username"]
    inlines = [ProfileInLine]
    

# Register
admin.site.register(User, UserAdmin)
#admin.site.register(Profile)


