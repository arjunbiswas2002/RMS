from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
# Create your models here.
a="9:00 am-10:00 am"
b="10:00 am-11:00 am"
c="11:00 am-12:00 pm"
d="12:00 pm-1:00 pm"

time_CHOICES = (
    (a, "9:00 am-10:00 am"),
    (b, "10:00 am-11:00 am"),
    (c, "11:00 am-12:00 pm"),
    (d, "12:00 pm-1:00 pm"),
)


class CustomUserRegistration(models.Model):
    username = models.CharField(max_length=50)
    full_name = models.CharField(max_length=100)
    password1 = models.CharField(max_length=128)
    password2 = models.CharField(max_length=128)

class Booking(models.Model):
    date = models.DateField()
    time= models.CharField(max_length=100,choices=time_CHOICES,default="1")
    name = models.CharField(max_length=50)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,10}$',
                                 message="Phone number must be entered in the format: '9999999999'. Up to 10 digits allowed.")
    phonenumber = models.CharField(validators=[phone_regex], max_length=13, verbose_name="Mobile", null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

class Contact(models.Model):
    name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=500)
    content = models.TextField()

    def __str__(self):
        return self.name

