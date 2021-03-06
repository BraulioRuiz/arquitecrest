from django.db import models
from django.utils import timezone

class Example(models.Model):
    name = models.CharField(max_length=254, null=False)
    year = models.IntegerField(null=False)
    delete = models.BooleanField(default=False)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Example'
# Create your models here.
