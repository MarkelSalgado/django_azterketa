from django.db import models

# Create your models here.
# Create your models here.
class Kotxeak(models.Model):
    id = models.AutoField(primary_key=True)
    matrikula = models.CharField(max_length=50)
    marka = models.CharField(max_length=50)
    modeloa = models.CharField(max_length=50)
    kolorea = models.CharField(max_length=50)
    alokatzeko_prezioa = models.CharField(max_length=50)

    def __str__(self):
        return '%s' % self.matrikula