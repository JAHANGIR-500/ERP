from django.db import models
class Resource(models.Model):
    id = models.AutoField(primary_key=True)  # Explicitly define the auto-incrementing ID
    RESOURCE_GROUPS = [
        ('Civil work Material', 'Civil work Material'),
        ('Sanitary work Material', 'Sanitary work Material'),
        ('Electrical work Material', 'Electrical work Material'),
     
    ]
    name_of_resource = models.CharField(max_length=255)  # Resource name    
    resource_unit = models.CharField(max_length=50)
    resource_group = models.CharField(max_length=30, choices=RESOURCE_GROUPS, verbose_name='Group of Resource')
    def __str__(self):
        return self.name_of_resource  


