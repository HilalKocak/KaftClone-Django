from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from page.views import index, carousel_create
from product.views import show_category

urlpatterns = [
    path('', index, name='index'), 
    path('<slug:category_slug>', show_category, name='show_category'), 
    path('admin/', admin.site.urls),
    path('manage/carousel_create',carousel_create, name='carousel_create' ),
    path("manage/", include("page.urls",)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
