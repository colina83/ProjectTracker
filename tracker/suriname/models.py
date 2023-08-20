from django.db import models

# Create your models here.

class Manager(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.first_name + " " + self.last_name

class Company(models.Model):
    name = models.CharField(max_length=30)
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
class Project(models.Model):
    
    STAGE = {
        ('Completed','Completed'),
        ('Planned', 'Planned'),
        ('Ongoing', 'Ongoing'),
    }
           
    name = models.CharField(max_length=30)    
    stage = models.CharField(max_length=20, choices=STAGE)
    products = models.ManyToManyField('Product', related_name='projects')
    
    def __str__(self):
        return self.name

class Product(models.Model):
    PRODUCTS_CHOICES = (
        ('A', 'Acquisition Deliverables'),
        ('FT', 'Fast-Track PSDM'),
        ('FI', 'Full-Integrity PSDM'),
        ('N', 'No Product')
    )
     
    code = models.CharField(max_length=2, choices=PRODUCTS_CHOICES, primary_key=True)
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    
class Status(models.Model):
    STATUS_CHOICES = (
        ('Data Review', 'Data Review'),
        ('Proposal', 'Proposal'),
        ('No Contact', 'No Contact'),
        ('Contacted', 'Contacted'),  
        ('Licensed','Licensed')      
    )
    
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    date = models.DateField(null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    
    @property
    def manager_name(self):
        return f"{self.company.manager.first_name} {self.company.manager.last_name}"
    
    
    def __str__(self):
        return self.status