from django.urls import path
# from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path('', views.PersonListView.as_view(), name='person_list'),
    path('<int:pk>/', views.PersonDetailView.as_view(), name='person_detail'),
]
