from django.db import models

class Nota(models.Model):
    title = models.CharField(max_length=100, blank=True)
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)