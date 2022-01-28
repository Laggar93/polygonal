from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from shop.views import handler404
from contact.views import form_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('form/', form_view, name='form'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(
    path('', include('index.urls')),
    path('', include('shop.urls')),
    path('', include('order_projects.urls')),
    path('', include('advice.urls')),
    path('', include('delivery.urls')),
    path('', include('contact.urls')),
    path('', include('map.urls')),
    path('', include('about.urls')),
    path('', include('base.urls')),
)

handler404 = handler404