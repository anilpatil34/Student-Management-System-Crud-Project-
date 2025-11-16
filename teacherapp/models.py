from django.db import models

# Create your models here.

class Teacher(models.Model):
    t_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.subject}" 