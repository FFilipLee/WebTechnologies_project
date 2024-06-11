from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('questions/', views.question_list, name='question_list'),
    path('questions/<int:question_id>/', views.question_detail, name='question_detail'),
    path('questions/<int:question_id>/post_answer/', views.post_answer, name='post_answer'),
    path('answers/<int:answer_id>/post_comment/', views.post_comment, name='post_comment'),
    path('answers/<int:answer_id>/like/', views.like_answer, name='like_answer'),
    path('ask/', views.post_question, name='post_question'),
    path('delete_answer/<int:answer_id>/', views.delete_answer, name='delete_answer'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('delete_question/<int:question_id>/', views.delete_question, name='delete_question'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('search/', views.search, name='search'),
    path('answers/<int:answer_id>/post_comment/', views.post_comment, name='post_comment'),
    path('question/<int:question_id>/like/', views.like_question, name='like_question'),
    path('question/<int:question_id>/dislike/', views.dislike_question, name='dislike_question'),
    path('answer/<int:answer_id>/like/', views.like_answer, name='like_answer'),
    path('answer/<int:answer_id>/dislike/', views.dislike_answer, name='dislike_answer'),
    path('question/<int:question_id>/calculate_likes/', views.calculate_question_likes, name='calculate_question_likes'),
    path('question/<int:question_id>/calculate_dislikes/', views.calculate_question_dislikes, name='calculate_question_dislikes'),
    path('profile/', views.profile, name='profile'),
]