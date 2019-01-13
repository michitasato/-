from django.urls import path
from .views import Index, get_data

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('api/', get_data, name='api')
]
