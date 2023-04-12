from django.shortcuts import render
from .models import Carousel
from django.contrib import messages
from .forms import CarouselModelForm

def index(request):
    context = dict()
    context['images'] = Carousel.objects.filter(status="published").exclude(cover_image='')
    return render(request, 'home/index.html', context)


def carousel_list(request):
    context=dict()
    context['carousel'] = Carousel.objects.all().order_by('-pk')
    return render(request, 'manage/carousel_list.html', context)

def carousel_update(request, pk):
    context=dict()
    item = Carousel.objects.get(pk=pk)
    context['form'] = CarouselModelForm(instance=item)
    return render(request, 'manage/carousel_create.html', context)


def carousel_create(request):
    context = dict()
    context['form'] = CarouselModelForm()
    #item = Carousel.objects.first()
    #context['form'] = CarouselModelForm(instance=item)

    if request.method =='POST':
        print(request.POST)
        print(request.FILES.get('cover_image'))
        form = CarouselModelForm(request.POST, files=request.FILES)
       
        if form.is_valid():
            form.save() # Bunu demeden veri tabanına kaydetmiyor :)
        messages.success(request, 'Birseyler eklendi ama neler oldu bilmiyorum')

    return render(request, 'manage/carousel_create.html', context)