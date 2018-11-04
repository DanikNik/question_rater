from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Person(models.Model):
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)

    nickname = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)

    avatar = models.ImageField(null=True, blank=True)

    rating = models.FloatField(null=True, blank=True, default=0.0)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name + ' ' + self.surname + '({})'.format(self.nickname)

    def get_absolute_url(self):
        return reverse('person_detail', args=[self.id])
