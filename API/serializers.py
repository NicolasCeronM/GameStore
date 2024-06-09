from gestionProducto.models import Producto,Plataforma
from rest_framework import serializers

class PlataformaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plataforma
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    plataforma = PlataformaSerializer(read_only=True)  ## Crea un serializador dentro de otro, osea que sale toda la informacion sobre su plataforma
    plataforma_id = serializers.PrimaryKeyRelatedField(queryset = Plataforma.objects.all(), source='plataforma') # Crea el campo para ingresar datos 
    nombre = serializers.CharField(required=True, min_length = 3) #Validacion al ingresar datos
    class Meta:
        model = Producto
        fields = '__all__'