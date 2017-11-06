from django.db import models


# Create your models here.
class Account(models.Model):
    user = models.OneToOneField('auth.User')   #link this field with Django User.
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER) # gender field
    balance = models.IntegerField(default=0)    # balance field

    def __str__(self):
        return self.user.get_full_name()    # return full name in admin site.