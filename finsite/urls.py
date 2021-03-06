from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('finapp.urls')),
    path('captcha/', include('captcha.urls')),

]
if settings.DEBUG:
    from django.urls import include, path

    urlpatterns = [

                      path('__debug__/', include('debug_toolbar.urls')),

                  ] + urlpatterns
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
