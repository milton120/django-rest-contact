from django.db import models
from django.conf import settings
# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
