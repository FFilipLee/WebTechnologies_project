from django.contrib import admin
from .models import User, Question, Answer, Comment, QuestionTag

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'email', 'joinDate')

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'postDate', 'closed', 'views', 'upvotes', 'downvotes')

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'postDate', 'views', 'upvotes', 'downvotes')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'question', 'answer', 'postDate', 'views')

@admin.register(QuestionTag)
class QuestionTagAdmin(admin.ModelAdmin):
    list_display = ('tag', 'question')
