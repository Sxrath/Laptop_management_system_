from django.contrib import admin
from .models import Condition, Laptop, Transaction, Reservation, feedback, Studentprofile,History

admin.site.register(Condition)
admin.site.register(Laptop)
admin.site.register(Transaction)
admin.site.register(Reservation)
admin.site.register(feedback)
admin.site.register(Studentprofile)
admin.site.register(History)