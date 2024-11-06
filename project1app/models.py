from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    skills = models.TextField(blank=True, null=True)
    contact_email = models.EmailField(max_length=254, blank=True, null=True)

    def __str__(self):
        return self.user.username


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    project_link = models.URLField(max_length=200, blank=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True, default='projects/default_project_image.jpg')

    def __str__(self):
        return self.title



class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    description = models.TextField()


class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    school_name = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    graduation_year = models.IntegerField()


class Certification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    certification_name = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    date_received = models.DateField()
