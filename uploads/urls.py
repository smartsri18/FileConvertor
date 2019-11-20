from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.generic import TemplateView

from uploads.core import views


urlpatterns = [
    # url(r'^$', views.home, name='home'),
    # url(r'^uploads/simple/$', views.simple_upload, name='simple_upload'),
    url(r'^$', views.redirect, name='home'),
    url(r'^uploads/md_to_html/$', views.md_to_html, name='md_to_html'),
    path("uploads/json_to_xml",views.json_to_xml,name="json_to_xml"),
    path("uploads/xaml_to_csv",views.xaml_to_csv,name="xaml_to_csv"),
    url(r'^admin/', admin.site.urls),
    url(r'^convert/',views.convert_view,name="convert_view"),
    path("convert_json_to_xml",views.convert_json_to_xml,name="convert_json_to_xml"),
    path("convert_xml_to_csv",views.convert_xml_to_csv,name="convert_xml_to_csv"),
    path("homepage/",TemplateView.as_view(template_name="index.html"),name="index"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
