from django.db import models
from django.contrib.auth.models import User

class note(models.Model):
    title = models.CharField(max_length=512, null=True)
    note = models.TextField(null=True)
    date = models.DateField(auto_now_add=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)