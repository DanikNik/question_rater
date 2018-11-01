from django.urls import path
from . import views

urlpatterns = [
    path('', views.CockpitIndexView.as_view(), name='cockpit_index'),
    # path('add_question/', views.CreateQuestionView.as_view(), name='question_create'),


]
