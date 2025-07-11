from django.db import models
class Material(models.Model):
    id = models.AutoField(primary_key=True)
    name_of_material = models.CharField(max_length=255)
    material_unit = models.CharField(max_length=100)
    type_of_material = models.CharField(max_length=100)
    group_of_material = models.CharField(max_length=100)
    def __str__(self):
        return self.name_of_material

