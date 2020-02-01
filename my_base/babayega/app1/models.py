from django.db import models


class PhoneContacts(models.Model):
    network = models.CharField(max_length=20)
    phone_number = models.IntegerField()


class Contact(models.Model):
    name = models.CharField(max_length=20)
    email_address = models.EmailField()
    text = models.TextField()
