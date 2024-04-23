from django.contrib import admin
from .models import User, Question, Answer, Comment, QuestionTag, QuestionLike, QuestionDislike, AnswerLike, AnswerDislike

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'email', 'hashedPassword', 'joinDate', 'admin')

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'userId', 'title', 'postDate', 'closed', 'views', 'upvotes', 'downvotes')

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'userId', 'questionId', 'content', 'postDate', 'views', 'upvotes', 'downvotes')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'userId', 'questionId', 'answerId', 'content', 'postDate', 'views')

@admin.register(QuestionTag)
class QuestionTagAdmin(admin.ModelAdmin):
    list_display = ('tag', 'questionId')

@admin.register(QuestionLike)
class QuestionLikeAdmin(admin.ModelAdmin):
    list_display = ('questionId', 'userId')

@admin.register(QuestionDislike)
class QuestionDislikeAdmin(admin.ModelAdmin):
    list_display = ('questionId', 'userId')

@admin.register(AnswerLike)
class AnswerLikeAdmin(admin.ModelAdmin):
    list_display = ('questionId', 'userId')

@admin.register(AnswerDislike)
class AnswerDislikeAdmin(admin.ModelAdmin):
    list_display = ('questionId', 'userId')
