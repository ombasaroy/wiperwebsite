from django.db import models


# Create your models here.
class Document(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    file = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return self.name


class Publication(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    file = models.FileField(upload_to='publications/')

    def __str__(self):
        return self.name

