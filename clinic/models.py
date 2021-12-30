from django.db import models


# Create your models here.
class ItemBase(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=16)
    gender = models.CharField(max_length=10)
    phonenumber = models.CharField(max_length=10)
    birthdate = models.DateField()


class Patient(ItemBase):
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Doctor(ItemBase):
    specialization = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Nurse(ItemBase):
    def __str__(self):
        return self.name


class Appointment(models.Model):
    doctorname = models.CharField(max_length=50)
    doctoremail = models.EmailField(max_length=50)
    patientname = models.CharField(max_length=50)
    patientemail = models.EmailField(max_length=50)
    appointmentdate = models.DateField(max_length=10)
    appointmenttime = models.TimeField(max_length=10)
    symptoms = models.CharField(max_length=100)
    status = models.BooleanField()
    prescription = models.CharField(max_length=200)

    def __str__(self):
        return self.patientname + " you have appointment with " + self.doctorname