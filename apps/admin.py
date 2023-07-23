from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display=['id','name','slug']
    prepopulated_fields={'slug':('name',)}


@admin.register(Variety)
class VarietyAdmin(admin.ModelAdmin):
    list_display=['id','title','food','photo']
    prepopulated_fields={'slug':('title',)}
