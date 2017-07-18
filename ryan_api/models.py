from django.db import models

# Create your models here.

class Run(models.Model):
    # distance ran in miles
    distance = models.FloatField(null=False)
    # date of the workout
    date = models.DateField(null=False)

    class Meta:
        db_table = 'runs'
        managed = True


class Read(models.Model):
    title = models.TextField(blank=False, null=False)
    author = models.TextField(blank=False, null=False)
    is_finished = models.BooleanField()

    class Meta:
        db_table = 'reads'
        managed = True
