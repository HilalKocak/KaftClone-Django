from product.models import Category
from page.views import STATUS
from page.models import Page

def nav_data(request):
    context = dict()
    context['categories'] = Category.objects.filter(status = STATUS).order_by('title')
    context['pages'] = Page.objects.filter(status = STATUS).order_by('title')
    return context