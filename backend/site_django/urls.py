from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from django.conf import settings
from django_email_verification import urls as email_urls

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('shop.urls', namespace='shop')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('account/', include('account.urls', namespace='account')),
    path('email/', include(email_urls), name='email-verification'),
    path('payment/', include('payment.urls', namespace='payment')),
    path('recommend/', include('recommend.urls', namespace='recommend')),
    path('api/', include('api.urls', namespace='api')),
    path('', views.index, name='index'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

