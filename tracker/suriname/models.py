from django.db import models

# Create your models here.
class Manager(models.Model):
    first_name = models.CharField(max_length=20, null=True)

    def __str__(self):
        return 

    def __unicode__(self):
        return 
