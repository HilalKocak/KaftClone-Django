from django.shortcuts import render
from .models import Carousel
from django.contrib import messages
from .forms import CarouselModelForm

def index(request):
    context = dict()
    context['images'] = Carousel.objects.filter(status="published")
    images = Carousel.objects.all()
    context['images'] = images
    return render(request, 'home/index.html', context)

def carousel_create(request):
    context = dict()
    context['form'] = CarouselModelForm()
    if request.method =='POST':
        print(request.POST)
        print(request.FILES.get('cover_image'))

        title = request.POST.get('title')
        carousel = Carousel.objects.create(title = title)
        carousel.save()
        messages.success(request, 'Birseyler eklendi ama neler oldu bilmiyorum')

    return render(request, 'manage/carousel_create.html', context)