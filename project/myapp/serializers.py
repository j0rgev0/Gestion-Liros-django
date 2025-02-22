from rest_framework import serializers
from .models import Libro, Autor

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'

class LibroSerializer(serializers.ModelSerializer):
    autor = AutorSerializer(read_only=True)
    autor_id = serializers.PrimaryKeyRelatedField(queryset=Autor.objects.all(), write_only=True, source='autor')
    
    class Meta:
        model = Libro
        fields = ['id', 'titulo', 'fecha_publi', 'genero', 'isbn', 'autor', 'autor_id']
