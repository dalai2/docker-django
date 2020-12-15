

from django.contrib import admin
from django.urls import path
from posts import views
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        route='',
        view=views.HomeView.as_view(),
        name='inicio'
    ),
    path(
        route='ilustraciones',
        view=views.TemplateView.as_view(template_name='images.html'),
        name='ilustraciones'
    ),
    path(
        route='animaciones',
        view=views.TemplateView.as_view(template_name='animation.html'),
        name='animaciones'
    ),
    path(
        route='contacto',
        view=views.TemplateView.as_view(template_name='animation.html'),
        name='animaciones'
    )    
] + static(prefix='static')
