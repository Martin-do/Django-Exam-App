from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.register, name="begin"),
    path("pre_exam", views.pre_exam, name="pre_exam"),
    path("process", views.process, name="start"),
    path("blog/index/", views.index, name="index"),
    path("blog/post/", views.postdet, name="post"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)