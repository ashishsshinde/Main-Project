from django.contrib import admin

from home.models import User
from home.models import contactForm
from home.models import call

# Register your models here.
admin.site.register(User)
admin.site.register(contactForm)
admin.site.register(call)

