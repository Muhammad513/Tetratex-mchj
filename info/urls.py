from django.urls import path
from .views import*

urlpatterns=[
    path('info/',info,name='info'),
    path('form/',form,name='form'),
    path('staff/',info,name='staff'),
    path('tabel/',tabel,name='tabel')


]