from django.shortcuts import redirect, render
from .models import Carousel, Page
from django.contrib import messages
from .forms import CarouselModelForm, PageModelForm
from slugify import slugify
from django.contrib.admin.views.decorators import staff_member_required

def index(request):
    context = dict()
    context['images'] = Carousel.objects.filter(status="published").exclude(cover_image='')
    return render(request, 'home/index.html', context)

def manage_list(request):
    context = dict()
    return render(request, 'manage/manage.html', context)

def page_list(request):
    context=dict()
    context['items'] = Page.objects.all().order_by('-pk')
    return render(request, 'manage/page_list.html', context)

def page_create(request):
    context = dict()
    context['title'] = "Page Create Form"
    context['form'] = PageModelForm()

    if request.method =='POST':
        form = PageModelForm(request.POST, files=request.FILES)
       
        if form.is_valid():
            item = form.save(commit = False) 
            print(item.title)
            item.slug = slugify(item.title)
            item.save()
        messages.success(request, 'Birseyler eklendi')

    return render(request, 'manage/form.html', context)

def page_update(request, pk):
    context=dict()
    item = Page.objects.get(pk=pk)
    context['title'] = f"{item.title} - pk:{item.pk} Page Create Form"
    context['form'] = PageModelForm(instance=item)

    if request.method == 'POST':
        form = PageModelForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            if item.slug == '':
                item.slug = slugify(item.title)
            item.save()
            messages.success(request, 'updated')
            return redirect('page_update', pk)
    return render(request, 'manage/form.html', context)

@staff_member_required
def page_delete(request, pk):
    context=dict()
    item = Page.objects.get(pk=pk)
    item.status = 'deleted'
    item.save()
    return redirect('page_list')


def carousel_list(request):
    context=dict()
    context['carousel'] = Carousel.objects.all().order_by('-pk')
    return render(request, 'manage/carousel_list.html', context)

def carousel_update(request, pk):
    context=dict()
    item = Carousel.objects.get(pk=pk)
    context['title'] = f"{item.title} - pk:{item.pk} Carousel Create Form"

    #item i bul, ve ekrana goster demek
    
    context['form'] = carousel_form(instance=item)

    if request.method == 'POST': # eger kullanici degisiklik yapip kaydederse
        form = CarouselModelForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            #return redirect('carousel_list')
            messages.success(request, 'updated')
            return redirect('carousel_update', pk)
    return render(request, 'manage/form.html', context)

def carousel_form(request=None, instance=None):
    if request:
        form = CarouselModelForm(request.POST, request.FILES, instance=instance)
    else:
        form = CarouselModelForm(instance=instance)
    return form

def carousel_create(request):
    context = dict()
    context['title'] = "Carousel Create Form"

    context['form'] = carousel_form()
    #item = Carousel.objects.first()
    #context['form'] = CarouselModelForm(instance=item)

    if request.method =='POST':
        print(request.POST)
        print(request.FILES.get('cover_image'))
        form = CarouselModelForm(request.POST, files=request.FILES)
       
        if form.is_valid():
            form.save() # Bunu demeden veri tabanına kaydetmiyor :)
        messages.success(request, 'Birseyler eklendi ama neler oldu bilmiyorum')

    return render(request, 'manage/carousel_form.html', context)