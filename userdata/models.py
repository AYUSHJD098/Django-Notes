from django.db import models

class note(models.Model):
    title = models.CharField(max_length=512, null=True)
    note = models.TextField(null=True)
    date = models.DateField(auto_now_add=True, null=True)