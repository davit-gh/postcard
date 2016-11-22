from django.db import models

# Create your models here.
class Contactus(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=False)
    description = models.TextField(blank=False)
    message_date = models.DateTimeField(auto_now_add=True, blank=True)
