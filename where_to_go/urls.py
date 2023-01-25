
from django.contrib import admin
from django.urls import path
from .views import home
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home)
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)

