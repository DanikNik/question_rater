from django.views.generic import ListView, DetailView
from .models import Person

class PersonListView(ListView):
    model = Person
    template_name = 'account/person_list.html'
    context_object_name = 'person_list'

class PersonDetailView(DetailView):
    model = Person
    template_name = 'account/person_detail.html'
    context_object_name = 'person'
