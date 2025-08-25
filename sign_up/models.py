from django.db import models

# Create your models here.
class Account(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True, null=False)
    password = models.CharField(max_length=100)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    HOBBIES_CHOICES =(
        ('Music', 'Music'),
        ('Sports', 'Sports'),
        ('Tracel', 'Tracel'),
        ('Movies', 'Movies'),
    )
    hobbies = models.CharField(max_length=20, choices=HOBBIES_CHOICES)
    SOURCE_OF_INCOME_CHOICES = (
        ('Employed', 'Employed'),
        ('Student', 'Student'),
        ('Business', 'Business'),
        ('Others', 'Others'),
    )
    source_of_income = models.CharField(max_length=20, choices=SOURCE_OF_INCOME_CHOICES)
    income = models.PositiveIntegerField(default=20)
    profile_pic = models.ImageField(upload_to='Profile_pic/', blank=True)
    age = models.PositiveIntegerField(default=18)
    bio = models.TextField(default='')
