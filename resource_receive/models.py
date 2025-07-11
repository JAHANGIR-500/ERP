from django.db import models
from project.models import Project
from resource.models import Resource

class ResourceReceive(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.CASCADE, default=1)
    resource_name = models.ForeignKey(Resource, on_delete=models.CASCADE, default=1)
    unit = models.CharField(max_length=50, blank=True)
    receive_date = models.DateField(verbose_name="Receive Date")
    channel_no = models.CharField(max_length=30, verbose_name="Channel No")
    receive_quantity = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        # Auto-fill unit from selected resource if not manually set
        if self.resource_name and not self.unit:
            self.unit = self.resource_name.resource_unit  # ✅ Correct field name
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Receive #{self.id} — {self.project_name.name_of_project} for {self.resource_name.name_of_resource}"



    




    



        
        

