from django.views.generic import ListView, DetailView, UpdateView
from .models import Person
from django.views.generic import CreateView
from catalog.assets.user_check_mixins import ProfileCheckMixin

class PersonListView(ProfileCheckMixin, ListView):
    model = Person
    template_name = 'account/person_list.html'
    context_object_name = 'person_list'


class PersonDetailView(ProfileCheckMixin, DetailView):
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


class PersonUpdateView(ProfileCheckMixin, UpdateView):
    model = Person
    fields = ['type']
    template_name = 'account/person_update.html'
    fields = [
        'nickname',
        'name',
        'surname',
    ]

    def get_object(self):
        return self.request.user.person
