from django.db import models

# Create your models here.

class Run(models.Model):
    # distance ran in miles
    distance = models.FloatField(null=False)
    # date of the workout
    date = models.DateField(auto_now=False, auto_add_now=False, null=False)

    class Meta:
        db_table = 'runs'
        managed = True


class Read(models.Model):
    book = models.TextField(blank=False, null=False)
    author = models.TextField(blank=False, null=False)
    is_finished = models.BooleanField()

    class Meta:
        db_table = 'reads'
        managed = True
