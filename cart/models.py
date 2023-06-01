from django.db import models
from django.contrib.auth.models import User
from product.models import Product
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver

# Create your models here.
DEFAULT_STATUS = "waiting"

STATUS = [
    # left side: DB
    # right side: human-readable name
    ('waiting', 'Bekleniyor'),
    ('sold', 'Satildi'),
    ('deleted', 'Silindi'),
]
class ShoppingCardItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField(max_length=5, default=0)

    is_deleted = models.BooleanField(default=False)
    createt_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product.title} price: {self.price} TL"

class ShoppingCard(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    session_key = models.CharField(max_length=32, blank=True, null=True)
    createt_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    items = models.ManyToManyField(ShoppingCardItem, blank=True)
    total_price =  models.FloatField(default=0)
    status =  models.CharField(
        default=DEFAULT_STATUS, 
        choices=STATUS,
        max_length=10,
    )
    def __str__(self):
        return f"PK: {self.pk} - Total: {self.total_price} TL - Status: {self.status}"

    def total_price_update(self):
        total_price = 0
        print(f"{self.total_price}")
        items = self.items.all()
        for item in items:
            if item.is_deleted == False:
                total_price += item.price
        self.total_price = total_price
        print(total_price)
        self.save()

@receiver(post_save, sender=ShoppingCardItem)
def shopping_card_item_receiver(sender, instance, created, *args, **kwargs):
    if created:
        instance.price = instance.product.price
        instance.save()
    instance.shoppingcard_set.last().total_price_update()
    print(kwargs)
    print(f"{'x' * 30}\nShoppingCardItem\n{'x' * 30}")
    print(instance.shoppingcard_set.last().total_price)


@receiver(m2m_changed, sender=ShoppingCard.items.through)
def shopping_card_receiver(sender, instance, *args, **kwargs):
    instance.total_price_update()
    print(args)
    print(kwargs)
    print(f"{'x' * 30}\nShoppingCard\n{'x' * 30}")