from django.db import models
from account.models import Person
from django.urls import reverse


class Question(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    raters = models.ManyToManyField(Person, through='questions.QuestionAnswer')
    # tags = models.ManyToManyField('Tag')

    # true_answer = models.BooleanField(null = True, blank = True)

    # date
    # expire_date
    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('question_detail', args=[self.id])


class QuestionAnswersLog(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    rating = models.FloatField()
    timestamp = models.DateTimeField(auto_now=True)

    @classmethod
    def rate_question(self, _question, _person, _rating):
        answer = self.objects.create(person=_person, question=_question, rating=_rating)
        return answer


class QuestionAnswer(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    # rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(100.0)])
    # timestamp = models.DateTimeField(auto_now=True)
    log = models.OneToOneField(QuestionAnswersLog, null=True, on_delete=models.CASCADE)

    @classmethod
    def set_log_entry(self, _log_entry):
        self.log = _log_entry


# class Tag(models.Model):
#     tag_name = models.CharField(max_length=30)
#
#     def __str__(self):
#         return self.tag_name
#
#     def get_absolute_url(self):
#         return reverse('question_by_tag_list', args=[self.id])
