#---------------Agregando librerias Framework--------------------
from rest_framework import routers,serializers,viewsets
#---------------Agregando Modelos--------------------------------
from Example.models import Example

class ExampleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Example
        fields = ('__all__')