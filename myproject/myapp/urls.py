from django.urls import path
from . import views
from . views import index, about

urlpatterns = [
    path('about/', views.about, name='about'),
    path('index/', views.index, name='index')
]