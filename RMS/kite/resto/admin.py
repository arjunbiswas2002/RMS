from django.contrib import admin
from .models import Booking
from .models import UserProfile
from .models import Contact


admin.site.register(Booking)
admin.site.register(UserProfile)
admin.site.register(Contact)

