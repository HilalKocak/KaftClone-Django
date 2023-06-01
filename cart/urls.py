from django.urls import path
from .views import shopping_card_item_add

urlpatterns = [
    path('add/<int:card_item_id>/', shopping_card_item_add, name='shopping_card_item_add'),
]