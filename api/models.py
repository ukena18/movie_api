from django.db import models

# Create your models here.


class Title(models.Model):
    title  = models.CharField(max_length=200)
    completed = models.BooleanField(default=False, null= True)

    def __str__(self):
        return self.title

