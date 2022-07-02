from django.contrib import admin
from .models import *


class VeganAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Vegan._meta.fields]

admin.site.register(User)
admin.site.register(Vegan, VeganAdmin)
admin.site.register(CO2Cal)
admin.site.register(Challenge)
admin.site.register(GroupPurchase)


