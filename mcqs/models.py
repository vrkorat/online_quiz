from django.db import models

# Create your models here.
class MCQ(models.Model):
    question=models.CharField(max_length=5000)
    ca=models.CharField(max_length=100)
    wa1=models.CharField(max_length=100)
    wa2=models.CharField(max_length=100)

    def __str__(self):
        return "coreect answer is : "+ self.ca