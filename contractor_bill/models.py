from django.db import models
class ContractorBill(models.Model):
    id = models.AutoField(primary_key=True)  # Unique ID (Auto-incremented)
    name_of_project = models.CharField(max_length=255)  # Detailed project name
    
    TYPE_CHOICES = [
        ('DEA', 'DEA'),
        ('New Project', 'New Project'),
    ]
    type_of_project = models.CharField(max_length=50, choices=TYPE_CHOICES)  # Dropdown menu (DEA/New Project)
    
    name_of_work = models.CharField(max_length=255)  # Work description
    
    WORK_UNIT_CHOICES = [
        ('Sft', 'Square Feet'),
        ('Cft', 'Cubic Feet'),
        ('Nos', 'Numbers'),
        ('Pcs', 'Pieces'),
    ]
    work_unit = models.CharField(max_length=50, choices=WORK_UNIT_CHOICES)  # Dropdown menu (Sft, Cft, Nos, Pcs)
    
    name_of_contractors_company = models.CharField(max_length=255)  # Contractor’s name
    quantity = models.PositiveIntegerField()  # Quantity of work done
    unit_rate = models.DecimalField(max_digits=10, decimal_places=2)  # Rate per unit
    
    # Computed field for Bill Amount
    @property
    def bill_amount(self):
        return self.quantity * self.unit_rate  # Calculates total bill
    
    def __str__(self):
        return f"{self.name_of_project} - {self.name_of_work}"

