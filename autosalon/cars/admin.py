from django.contrib import admin
from .models import Brand, Car


admin.site.register(Brand)
class BrandModel (admin.ModelAdmin):
    list_display =('name', 'country')
admin.site.register(Car)

class CarModel(admin.ModelAdmin):
    list_display =('brand','model_name','year','price','description')
    search_fields =('brand','model_name')
    list_filter = ('year',)