from django.urls import path
from . import views

urlpatterns = [
    path('scrapEmpresa/', views.scrapEmpresa, name='scrapEmpresa'),
]
