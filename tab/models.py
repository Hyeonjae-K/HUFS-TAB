from django.db import models


class Contents(models.Model):
    subject = models.CharField(max_length=16)
    content = models.TextField()
    create_date = models.DateTimeField()
