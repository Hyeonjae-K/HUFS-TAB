from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError


class Post(models.Model):
    subject = models.CharField(max_length=16)
    content = models.TextField()
    main_image = models.ImageField(
        upload_to='postimages', blank=True, null=True)
    create_date = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.subject


class Application(models.Model):
    def _validate_file(value):
        value = str(value)
        if value.endswith('.pdf') or value.endswith('.doc') or value.endswith('.docx') or value.endswith('.txt'):
            return value
        raise ValidationError("지원하지 않는 파일 형식입니다.")

    def _set_file_path(instance, filename):
        file_format = filename.split('.')[-1]
        return f'applications/%Y-%m/{instance.studentnumber}_{instance.name}.{file_format}'

    name = models.CharField(max_length=8)
    studentnumber = models.CharField(max_length=16)
    phonenumber = models.CharField(max_length=11)
    file_path = models.FileField(upload_to=_set_file_path,
                                 validators=[_validate_file])
    create_date = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Application'
        verbose_name_plural = 'Applications'

    def __str__(self):
        return f'{self.studentnumber}_{self.name}'
