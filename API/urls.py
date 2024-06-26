from django.urls import path, include
from .viewSerializer import ProductoViewset
from rest_framework import routers

router = routers.DefaultRouter()

router.register('producto',ProductoViewset)

#Urls de la API
urlpatterns = [
    path('', include(router.urls)),
]