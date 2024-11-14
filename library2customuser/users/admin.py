from django.contrib import admin

from users.models import Users

admin.site.register(Users)

from users.models import CustomUser

admin.site.register(CustomUser)
