from django.db import models

# Create your models here.
class Visits(models.Model):
    class Meta:
        ordering: ["id"]
    ip = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
