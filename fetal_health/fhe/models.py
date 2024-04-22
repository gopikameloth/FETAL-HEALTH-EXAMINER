from django.db import models
class User(models.Model):
    # Model fields here

    class Meta:
        app_label = 'fhe'

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    specialisation = models.CharField(max_length=100)
    ph_no = models.CharField(max_length=20)
    hospital_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

