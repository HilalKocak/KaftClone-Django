from django.contrib import admin
from django.urls import path
from page.views import index, carousel_create
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'), 
    path('admin/', admin.site.urls),
    path('manage/carousel_create',carousel_create, name='carousel_create' )
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
