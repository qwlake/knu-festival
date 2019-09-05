from django.db import models

class Progress(models.Model):
    
    percentage = models.IntegerField(default=0)
        
    def __str__ (self):
        return "Progress bar"