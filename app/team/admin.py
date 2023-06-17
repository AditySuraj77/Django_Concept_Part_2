from django.contrib import admin
from .models import Player
from .models import Team

class Playerteam(admin.ModelAdmin):
    list_display = ('name','age','detail')

admin.site.register(Player,Playerteam)

class worldteam(admin.ModelAdmin):
    list_display = ('t_name','t_origin','t_desc','t_file')

admin.site.register(Team,worldteam)
# Register your models here.
