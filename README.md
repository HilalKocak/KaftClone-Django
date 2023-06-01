## E commercial web site with Django
This website is a clone of the commercial site www.kaft.com. Adding and removing products to the cart are performed by the backend. The html templates side will be completed soon.
In this application, products are added and updated to the site. At the same time, creating the user's basket and updating the basket were performed with django.

### Using techs
- Djnago ORM
- Django Middleware and Context Processor
- session_key
- django signals


### Queries used in the project
```
user = User.objects.get(username="hk@hk.com")
ShoppingCard.objects.filter(user = user, status="waiting)
ShoppingCard.objects.filter(user = user, status="waiting).count()
ShoppingCard.objects.create(user=user)
```