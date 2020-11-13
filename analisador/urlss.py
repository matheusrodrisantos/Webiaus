from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
   path('analise-grafico/',views.func_test, name = "analise-grafico"),
   path('upload/',views.upload, name = "upload")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)