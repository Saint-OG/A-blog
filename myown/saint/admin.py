from django.contrib import admin
from .models import Students



# Register your models here.
class Display (admin.ModelAdmin):
    list_display= ('dob', 'first_name', 'last_name', 'sex')


admin.site.register(Students)