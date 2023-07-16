from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from Flexor_portfolio import settings
from app1.views import blog

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('app1.urls')),
    path("", include('app2.urls')),
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)