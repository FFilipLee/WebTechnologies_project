from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('questions/', views.question_list, name='question_list'),
    path('questions/<int:pk>/', views.question_detail, name='question_detail'),
    path('ask/', views.post_question, name='ask_question'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
]