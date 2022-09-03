from django.db import models
from django.urls import reverse

# Create your models here.
class CrudModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def get_absolute_url(self):
        return reverse('detail_view', kwargs={'id': self.id})
    

    def __str__(self):
        return self.title
