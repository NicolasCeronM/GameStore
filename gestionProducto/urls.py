from django.urls import path
from . import views

urlpatterns = [
    path('',views.juegos, name='juegos'),
    path('detalle_juego/<int:producto_id>',views.detalle_juego, name='detalle_juego'),
    
]