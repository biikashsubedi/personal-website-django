from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),

    # backend
    path('system/', include('apps.backend.user.urls')),
    path('system/', include('apps.backend.home.urls')),
    path('system/portfolio/', include('apps.backend.portfoloi.urls')),
    path('system/profiles/', include('apps.backend.profiles.urls')),
    path('system/', include('apps.backend.resume.urls')),
    path('system/contact-us/', include('apps.backend.contact.urls')),
    path('system/analytic/', include('apps.backend.analyticData.urls')),
    path('system/jobs/', include('apps.backend.jobApply.urls')),
    path('system/shift/', include('apps.backend.shift.urls')),

    # frontend
    path('', include('apps.frontend.home.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
