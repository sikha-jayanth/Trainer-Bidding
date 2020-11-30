from django.db import models
from institute.models import Skills,Requirements
# Create your models here.
class PersonProfile(models.Model):
    user=models.CharField(max_length=100)
    name=models.CharField(max_length=120)
    skill=models.ForeignKey(Skills, on_delete=models.CASCADE)
    years_of_experience=models.IntegerField(default=0)
    qualification=models.CharField(max_length=120)
    cgpa=models.DecimalField(max_digits=2, decimal_places=1)
    university=models.CharField(max_length=120)
    email=models.EmailField()
    phone=models.CharField(max_length=12)
    place=models.CharField(max_length=120)
    address=models.CharField(max_length=200)
    def __str__(self):
        return self.name


class Application(models.Model):
    jobid = models.CharField(max_length=120)
    job_title = models.CharField(max_length=120)
    user = models.CharField(max_length=100)
    skill = models.CharField(max_length=120)
    location=models.CharField(max_length=120)
    name = models.CharField(max_length=120)

    years_of_experience = models.IntegerField(default=0)
    qualification = models.CharField(max_length=120)
    cgpa = models.DecimalField(max_digits=2, decimal_places=1)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    choices = (
        ("Applied", "Applied"), ("Processing", "Processing"), ("Rejected", "Rejected"), ("Selected", "Selected")
    )
    status = models.CharField(max_length=100, choices=choices, default="Applied")


