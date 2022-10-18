from django.db import models

# Create your models here.
class Pertsonak(models.Model):
    id = models.AutoField(primary_key=True)
    izena = models.CharField(max_length=50)
    abizena = models.CharField(max_length=50)
    dni = models.CharField(max_length=9)
    alokagai_daukan_kotxearen_id = models.CharField(max_length=3)

    def __str__(self):
        return '%s' % self.izena