from django.contrib import admin
from .models import Category, Product
# Register your models here.



class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = (
        'pk',
        'title',
        'slug',
        'gender',
        'status', 
        'updated_at',
    )
    list_filter = ('status', 'gender',)
    list_editable = (
        'title',
        'status', 
    )



class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = (
        'pk',
        'title',
        'slug',
        'is_home',
        'cover_image',
        'price',
        'stock',
        'status', 
        'updated_at',
    )
    list_filter = ('status',)
    list_editable = ( # Hic iceri girmeden editleyebilecegimiz fieldlar
        'title',
        'status', 
        'is_home',
    )

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)

