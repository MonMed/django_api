from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    tutor = models.CharField(max_length =100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name
