from django.views.generic import ListView, DetailView
from .models import Person
from django.views.generic import CreateView

class PersonListView(ListView):
    model = Person
    template_name = 'account/person_list.html'
    context_object_name = 'person_list'


class PersonDetailView(DetailView):
    model = Person
    template_name = 'account/person_detail.html'
    context_object_name = 'person'


class PersonCreateView(CreateView):
    model = Person
    template_name = 'account/person_create.html'
    fields = [
        'nickname',
        'name',
        'surname',
        # 'avatar'
    ]

    def form_valid(self, form):
        person = form.save(commit=False)
        person.user = self.request.user
        return super(PersonCreateView, self).form_valid(form)
