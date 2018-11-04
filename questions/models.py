from django.db import models
from account.models import Person
from django.urls import reverse

from catalog.assets.rating_rebase import ar_avg


class Question(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    raters = models.ManyToManyField(Person, through='questions.QuestionAnswer')
    tags = models.ManyToManyField(to='Tag', related_name='questions', verbose_name='Tags')

    is_expired = models.BooleanField(default=False)
    true_answer = models.BooleanField(null=True, blank=True, default=None)

    # date
    # expire_date
    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('question_detail', args=[self.id])

    def rebase_user_ratings(self):
        self.is_expired = True
        self.save()
        for person in self.raters.all():
            answer_value = QuestionAnswer.objects.get(question=self, person=person).log.rating
            person.rating = +ar_avg(answer_value, (100 if self.true_answer else 0))
            person.save()


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

    def set_log_entry(self, _log_entry):
        self.log = _log_entry


class Tag(models.Model):
    tag_name = models.SlugField(unique=True)

    def __str__(self):
        return self.tag_name

    def get_absolute_url(self):
        return reverse('question_by_tag_list', )

    class Meta:
        verbose_name = 'Tag'
