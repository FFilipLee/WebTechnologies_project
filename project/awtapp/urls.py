from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('questions/', views.question_list, name='question_list'),
    path('questions/<int:pk>/', views.question_detail, name='question_detail'),
    path('ask/', views.ask_question, name='ask_question'),
]