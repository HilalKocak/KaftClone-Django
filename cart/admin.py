from django.contrib import admin
from cart.models import ShoppingCard, ShoppingCardItem
# Register your models here.

admin.site.register(ShoppingCard)
admin.site.register(ShoppingCardItem)