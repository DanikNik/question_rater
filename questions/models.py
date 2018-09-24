from django.db import models
from account.models import Person

class Question(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)



class QuestionAnswers(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    rating = models.FloatField()

