from django.urls import path
from .views import index

urlpatterns = [
    path('perfiles/', index.as_view(), name='lista_perfiles'),
]
