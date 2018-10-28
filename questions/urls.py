from django.urls import path
# from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path('', views.QuestionListView.as_view(), name='question_list'),
    path('<int:pk>/', views.QuestionDetailView.as_view(), name='question_detail'),
    # path('tag/<int:pk>', views.QuestionByTagListView.as_view(), name='question_by_tag_list'),
]
