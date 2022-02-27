from django.db import models



#just for testing it is dummy model that i will not use
class Title(models.Model):
    title  = models.CharField(max_length=200)
    completed = models.BooleanField(default=False, null= True)

    def __str__(self):
        return self.title

