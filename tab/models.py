from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError


class Contents(models.Model):
    subject = models.CharField(max_length=16)
    content = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)


class Applications(models.Model):
    def _validate_file(value):
        value = str(value)
        if value.endswith('.pdf') or value.endswith('.doc') or value.endswith('.docx') or value.endswith('.txt'):
            return value
        raise ValidationError("Not suppor file format")

    name = models.CharField(max_length=8)
    studentnumber = models.CharField(max_length=16)
    phonenumber = models.CharField(max_length=11)
    path = models.FileField(upload_to='applications/%Y-%m',
                            validators=[_validate_file])
    create_date = models.DateTimeField(default=timezone.now)
