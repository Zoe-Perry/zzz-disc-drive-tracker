from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Character(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='characters')
    name = models.TextField() 
    image = models.ImageField(upload_to='characters')

    def __str__(self):
        return self.name.name if self.name else 'No Name'
    
class Disc(models.Model):
    id = models.IntegerField(primary_key=True)
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='disc_drive')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='disc_drive')
    set = models.TextField()
    main_stat = models.TextField()
    stat_1 = models.IntegerField()
    stat_2 = models.IntegerField()
    stat_3 = models.IntegerField()
    stat_4 = models.IntegerField()

    def __str__(self):
        return f"Disc Drive for {self.character.name}"