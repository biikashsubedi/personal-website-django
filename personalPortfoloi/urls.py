from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),

    # backend
    path('', include('apps.backend.user.urls')),
    path('', include('apps.backend.home.urls')),
    path('portfolio/', include('apps.backend.portfoloi.urls')),
    path('profiles/', include('apps.backend.profiles.urls')),
    path('', include('apps.backend.resume.urls')),

    # frontend
    path('', include('apps.frontend.home.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
