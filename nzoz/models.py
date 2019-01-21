from django.db import models

class Clinic(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Specialty(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Day(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Specialist(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Schedule(models.Model):
    hourFrom = models.TimeField()
    hourTo = models.TimeField()
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)

    


