from django.urls import path, include
from . import views
from rest_framework import routers
from .API.viewSerializer import ProductoViewset

router = routers.DefaultRouter()
router.register('producto',ProductoViewset)



urlpatterns = [
    path('',views.juegos, name='juegos'),
    path('detalle_juego/<int:producto_id>',views.detalle_juego, name='detalle_juego'),
    path('api/', include(router.urls)),
    
]