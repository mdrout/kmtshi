from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from kmtshi.coordinates import great_circle_distance

@python_2_unicode_compatible #unicode support for Python 2
class Field(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    subfield = models.CharField(max_length=20)
    def __str__(self):
        return self.subfield

@python_2_unicode_compatible #unicode support for Python 2
class Quadrant(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

@python_2_unicode_compatible #unicode support for Python 2
class Classification(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

@python_2_unicode_compatible #unicode support for Python 2
class Candidate(models.Model):
    id = models.AutoField(primary_key=True)
    ra = models.FloatField()
    dec = models.FloatField()
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    quadrant = models.ForeignKey(Quadrant, on_delete=models.CASCADE)
    classification = models.ForeignKey(Classification, on_delete=models.CASCADE)
    date_disc = models.FloatField(default=160000)
    name = models.CharField(max_length=100,default="KSP-%s")
    def __str__(self):
        return self.name

    def is_same_target(self, candidate):
        """
        Figure out if two candidates are the same.
        :param candidate: candidate to compare
        :return: bool: True if the candidates have the same position (within 1")

        Notes
        -----
        We consider two targets to be the same if their positions are within 1" of each other.
        """
        return great_circle_distance(self.ra, self.dec,
                                     candidate.ra, candidate.dec) < (1.0 / 3600.0)
