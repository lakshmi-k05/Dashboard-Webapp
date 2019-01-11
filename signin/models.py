from django.db import models

class Members(models.Model):
    usn=models.CharField(max_length=40)
    pwd=models.CharField(max_length=30)
