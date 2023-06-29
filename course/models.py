from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=100)
    descrition = models.CharField(max_length=500)
    language = models.CharField(max_length=100)
    programming = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    creator = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    price = models.CharField(max_length=100)

class Add(models.Model):
    name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
