from django import forms
from .models import Carousel


class CarouselModelForm(forms.ModelForm):

    class Meta:
        model=Carousel
        fields=[  
            'title',
            'cover_image',
            
            ]
          
        