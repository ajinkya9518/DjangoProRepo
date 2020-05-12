from django.contrib import admin
from secapp.models import  State


# Register your models here.
class StateAdmin(admin.ModelAdmin):
    list_display = ["statename","statecode","state_cm"]
admin.site.register(State,StateAdmin)