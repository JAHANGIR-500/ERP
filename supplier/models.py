from django.db import models
class Supplier(models.Model):
    id = models.AutoField(primary_key=True)  # Auto-incrementing supplier ID
    name_of_supplier = models.CharField(max_length=255)  # Name of the supplier
    supplier_address = models.CharField(max_length=500)  # Address as CharField
    supplier_contact_no = models.CharField(max_length=20)  # Contact number
    def __str__(self):
        return self.name_of_supplier

