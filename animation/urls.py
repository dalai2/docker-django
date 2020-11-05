

from django.contrib import admin
from django.urls import path
from posts import views
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        route='',
        view=views.TemplateView.as_view(template_name='home.html'),
        name='home'
    ),

]
