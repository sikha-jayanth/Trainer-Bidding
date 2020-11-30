from django.db import models

# Create your models here.
class Skills(models.Model):
    skill=models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.skill


class Requirements(models.Model):
    jobid=models.CharField(unique=True,max_length=50)
    job_title=models.CharField(max_length=120)
    skill_needed = models.ForeignKey(Skills, on_delete=models.CASCADE)
    years_of_experience=models.IntegerField(default=0)
    location=models.CharField(max_length=120)
    rate_per_hour=models.IntegerField(default=500)
    vacancies=models.IntegerField(default=1)
    def __str__(self):
        return self.job_title