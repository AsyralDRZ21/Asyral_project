from django.contrib import admin
from .models import Hall, Lecturer, Program, Event

# Register your models here.
admin.site.register(Hall)
admin.site.register(Lecturer)
admin.site.register(Program)
admin.site.register(Event)