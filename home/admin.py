from django.contrib import admin
from home.models import Contact
from home.models import login
from home.models import signup
from home.models import welcome
# Register your models here.
admin.site.register(Contact)
admin.site.register(login)
admin.site.register(signup)
admin.site.register(welcome)