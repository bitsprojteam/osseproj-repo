from rest_framework import serializers
from .models import vet

# class clinicSerializers(serializers.ModelSerializer):
#
#     class Meta:
#         model=clinic
#         fields='__all__'

class vetSerializers(serializers.ModelSerializer):

    class Meta:
        model=vet
        fields=('vetID','vet_firstname','vet_lastname')
