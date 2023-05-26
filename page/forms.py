from django import forms
from .models import Carousel, Page


class CarouselModelForm(forms.ModelForm):

    class Meta:
        model=Carousel
        fields=[  
            'title',
            'cover_image',
            'status',
            ]
          
class PageModelForm(forms.ModelForm):
    class Meta:
        model= Page
        fields = [
            'title',
            'cover_image',
            'content',
            'status',
        ]  