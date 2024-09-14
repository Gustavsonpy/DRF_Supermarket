from django.db import models

class UserBase(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.email
    
