from django.urls import path
from . import views

urlpatterns = [
    path('', views.CockpitIndexView.as_view(), name='cockpit_index'),

]
