from django.db import models
from account.models import Person
from django.urls import reverse


class Question(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    raters = models.ManyToManyField(Person, through='QuestionAnswers')


    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('question_detail', args=[self.id])


class QuestionAnswers(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    rating = models.FloatField()

    @classmethod
    def rate_question(self, _question, _person, _rating):
        answer = self.objects.create(person=_person, question=_question, rating=_rating)
        return answer
