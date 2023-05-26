from django.contrib import admin
from .models import Page, Carousel


class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = (
        'pk',
        'title',
        'slug',
        'status', 
        'updated_at',
    )
    list_filter = ('status', )
    list_editable = (
        'title',
        'status', 
    )


admin.site.register(Page, PageAdmin)


class CarouselAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'cover_image',
        'status',
 
    )
 

admin.site.register(Carousel, CarouselAdmin)