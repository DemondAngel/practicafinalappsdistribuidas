from django.db import models

# Create your models here.
class Classes(models.Model):
    """
        Mesa de clase masculina
    """

    title = models.CharField(max_length=32)
    m = models.ManyToManyField("Teachers")

class Teachers(models.Model):
    """
        Mesa docente femenina
    """

    name = models.CharField(max_length=32)

class Student(models.Model):
    username = models.CharField(max_length=32)
    age = models.IntegerField()
    gender = models.BooleanField()
    cs = models.ForeignKey(Classes, on_delete = models.CASCADE)
