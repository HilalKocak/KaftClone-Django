from django.shortcuts import render, redirect
from .models import ShoppingCard, ShoppingCardItem

def shopping_card_item_add(request, card_item_id):
    if request.user.is_authenticated:
        user = request.user
        shopping_cart = ShoppingCard.objects.filter(user=user, status="waiting")
        if  shopping_cart.count() > 0:
            shopping_cart = shopping_cart.last()
        else:
            shopping_cart = ShoppingCard.objects.create(user=user)
        
        shopping_cart.session_key = request.session.session_key
        item = ShoppingCardItem.objects.get(pk=card_item_id)
        print(item)
        shopping_cart.items.add(item)
        shopping_cart.total_price_update()
        shopping_cart.save()
    return redirect('/')