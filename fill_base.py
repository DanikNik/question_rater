#! venv//bin/python

import sys
import os
import django
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ['DJANGO_SETTINGS_MODULE'] = 'question_rater.settings'
django.setup()

# from yourapp.models import your_model
from account.models import Person
from questions.models import Question

for i in range(10):
    Person.objects.create(name='Person', surname=str(i), nickname="Person_{}".format(str(i)))
    Question.objects.create(title="Question #{}".format(str(i)), description="Question #{} descr".format(str(i)))