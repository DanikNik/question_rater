from django.views.generic.edit import CreateView, FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.views.generic import View

'''New person view was moved to account app'''
# class NewPersonView(CreateView):
#     model = Person
#     template_name = 'registration/person_create.html'
#     fields = [
#         'name',
#         'surname',
#         'last_name',
#         'place_of_study',
#         'group_number',
#         'place_of_work',
#         'job_position',
#         'birth_date',
#         'vk_link',
#         'fb_link',
#         'google_link',
#         'tg_link',
#         'phone_number',
#         'type'
#     ]
#
#     def form_valid(self, form):
#         person = form.save(commit=False)
#         person.user = self.request.user
#         return super(NewPersonView, self).form_valid(form)

# class NewPersonView(FormView):
#     template_name = 'registration/person_create.html'
#
#     def __init__(self):
#         self.user_id = 0
#
#     form_class = NewPersonForm
#     success_url = '/account/'
#
#     def form_valid(self, form):
#         person=form.save(commit=False)
#         person.user = self.request.user
#         person.save()
#         return super(NewPersonView, self).form_valid(form)
#
#     def get(self, request, user_id):
#         self.user_id = user_id
#         template = loader.get_template(self.template_name)
#         return HttpResponse(template.render({'user_id': user_id, 'form': NewPersonForm()}, request, ))


class RegisterFormView(FormView):
    form_class = UserCreationForm

    template_name = "registration/register.html"

    def form_valid(self, form):
        self.user = form.save()
        print(self.user)
        login(self.request, self.user)
        self.success_url = "/auth/login/"
        return super(RegisterFormView, self).form_valid(form)

# Create your views here.

#
# class LoginFormView(FormView):
# TODO: запилить кастомный логин, чтобы редиректило в личный кабинет
#     form_class = AuthenticationForm
#
#     template_name = "registration/login.html"
#     success_url = '/events'
#     def form_valid(self, form):
#         self.user = form.get_user()
#
#         login(self.request, self.user)
#         self.success_url = '/account/'+str(self.user.id)
#         return super(LoginFormView, self).form_valid(form)
