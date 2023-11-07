from django.db import models


class goal(models.Model):
    subject = models.CharField(max_length=100)
    content = models.TextField()
    create_date = models.CharField(max_length=30)
    end_date = models.CharField(max_length=30)
    

class cle_gl(models.Model):
    subject = models.CharField(max_length=100)    
    cre_date = models.CharField(max_length=30)
    end_date = models.CharField(max_length=30)
    
# Create your models here.
