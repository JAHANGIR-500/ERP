from django.db import models
from project.models import Project
from material.models import Material
class MaterialReceive(models.Model):
    id = models.AutoField(primary_key=True)
    project_name = models.ForeignKey(Project, on_delete=models.CASCADE, default=1)
    material_name = models.ForeignKey(Material, on_delete=models.CASCADE, default=1)
    unit = models.CharField(max_length=50, blank=True)
    material_type = models.CharField(max_length=100, blank=True)
    material_group = models.CharField(max_length=100, blank=True)
    receive_date = models.DateField(verbose_name="Receive Date")
    channel_no = models.CharField(max_length=30, verbose_name="Channel No")
    receive_quantity = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        if self.material_name:
            self.unit = self.material_name.material_unit
            self.material_type = self.material_name.type_of_material
            self.material_group = self.material_name.group_of_material
        super().save(*args, **kwargs)
    def __str__(self):
        return f"Receive #{self.id} — {self.project_name.name_of_project} | {self.material_name.name_of_material}"
