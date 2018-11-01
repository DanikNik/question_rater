from django.urls import path
# from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path('list', views.QuestionListView.as_view(), name='question_list'),
    path('<int:pk>/', views.QuestionDetailView.as_view(), name='question_detail'),
    # path('list/<slug:tag>', views.QuestionListView.as_view(), name='question_list'),
]
