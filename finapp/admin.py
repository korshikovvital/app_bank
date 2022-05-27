from django.contrib import admin
from .models import Category,Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name','published')
    list_editable = ('published',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name','category','profit','link')
    list_editable = ('link',)
    list_filter = ('category','profit')


admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)


