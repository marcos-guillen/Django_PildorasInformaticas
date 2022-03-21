from django.urls import path
from . import views

from django.conf.urls.static import static

urlpatterns = [
    path('',views.blog, name='Blog'),
    path('categoria/<categoria_id>/',views.categoria,name='categoria')
]

