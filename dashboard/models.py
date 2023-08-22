from django.db import models

from users.models import User


class Skills(models.Model):
    name = models.CharField(max_length=255)


class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resumes')
    name = models.CharField(max_length=255, null=True, blank=True)
    pdf_file = models.FileField(upload_to='pdf_files', null=True, blank=True)
    skills = models.ManyToManyField(Skills, blank=True, null=True, related_name='skills')

    def __str__(self):
        return self.name
