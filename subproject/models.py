from django.db import models

# Create your models here.

class Hall(models.Model):
    HallID=models.CharField(max_length=128,primary_key=True)
    HallName=models.TextField()
    Capacity=models.IntegerField()

class Lecturer(models.Model):
    LecturerID=models.CharField(max_length=128,primary_key=True)
    LecturerName=models.TextField()
    LecturerPass=models.TextField(max_length=128)

class Program(models.Model):
    ProgramID = models.CharField(max_length=4, primary_key=True) 
    ProgramName = models.TextField()

class Event(models.Model):
    EventID=models.CharField(max_length=128,primary_key=True)
    EventDate=models.DateField(blank=True,null=True)
    EventTime=models.TimeField(blank=True,null=True)
    HallID=models.ForeignKey(Hall, on_delete=models.CASCADE)
    ProgramID = models.ForeignKey(Program, on_delete=models.CASCADE)
    LecturerID = models.ForeignKey(Lecturer, on_delete=models.CASCADE)





    




