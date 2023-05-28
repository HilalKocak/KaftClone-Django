from django.shortcuts import render
from .models import Category, Product
from django.shortcuts import get_object_or_404

# Create your views here.

def show_category(request, category_slug):
    context = dict()
    context['category'] = get_object_or_404(Category, slug=category_slug)
    context['categories'] = Category.objects.filter(status = 'published').order_by('title')

    context['items'] = Product.objects.filter(category=context['category'],
                                              status = 'published',
                                              stock__gte = 1)
    
    return render(request, 'product/category_show.html', context)
    