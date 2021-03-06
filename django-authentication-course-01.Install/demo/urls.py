from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import re
from core.views import home, SignUpView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="home"),
    path('accounts/', include('allauth.urls')),
    path("signup/", SignUpView.as_view(), name="signup"),
    path('accounts/', include('django.contrib.auth.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)