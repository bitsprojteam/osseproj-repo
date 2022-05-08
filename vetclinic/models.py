from django.db import models
from .utils import str_uuid

# class clinic(models.Model):
#     #clinicID = models.UUIDField(primary_key = True,default = str(uuid.uuid4()),editable = False)
#     clinic_name = models.CharField(max_length=30)
#     clinic_address = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.clinic_name

class vet(models.Model):
    vetID = models.UUIDField(default=str_uuid,editable = False,unique=True)
    vet_firstname = models.CharField(max_length=30)
    vet_lastname = models.CharField(max_length=50)

    def __str__(self):
        return self.vet_firstname
