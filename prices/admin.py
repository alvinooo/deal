from django.contrib import admin

from .models import *

admin.site.register(Item)
admin.site.register(Store)
admin.site.register(ItemInstance)
admin.site.register(CurrentBest)
admin.site.register(Recipes)
admin.site.register(Trip)
