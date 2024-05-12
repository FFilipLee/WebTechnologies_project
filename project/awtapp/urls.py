from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('questions/', views.question_list, name='question_list'),
    path('questions/<int:pk>/', views.question_detail, name='question_detail'),
    path('questions/<int:question_id>/post_answer/', views.post_answer, name='post_answer'),
    path('answers/<int:answer_id>/post_comment/', views.post_comment, name='post_comment'),
    path('ask/', views.post_question, name='post_question'),
    path('delete_answer/<int:answer_id>/', views.delete_answer, name='delete_answer'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('delete_question/<int:question_id>/', views.search_question, name='delete_question'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
]