from django.db import models

class Monster(models.Model):
    id = models.AutoField(primary_key=True, db_column='Column1')
    name = models.CharField(max_length=200)
    alignment = models.CharField(max_length=50)
    hit_points = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'monsters'
        managed = False

    def __str__(self):
        return self.name
    
class Equipment(models.Model):
    id = models.AutoField(primary_key=True, db_column='Column1')
    name = models.CharField(max_length=200)
    
    class Meta:
        db_table = 'equipment'
        managed = False

    def __str__(self):
        return self.name
