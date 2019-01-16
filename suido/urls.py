from django.urls import path
from .views import Index, PostImport

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('upload/', PostImport.as_view(), name='upload')
]
