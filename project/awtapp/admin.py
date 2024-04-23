from django.contrib import admin
from .models import User, Question, Answer, Comment, QuestionTag, QuestionLikes, QuestionDislikes, AnswerLikes, AnswerDislikes

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

@admin.register(QuestionLikes)
class QuestionLikesAdmin(admin.ModelAdmin):
    list_display = ('questionId', 'userId')

@admin.register(QuestionDislikes)
class QuestionDislikesAdmin(admin.ModelAdmin):
    list_display = ('questionId', 'userId')

@admin.register(AnswerLikes)
class AnswerLikesAdmin(admin.ModelAdmin):
    list_display = ('questionId', 'userId')

@admin.register(AnswerDislikes)
class AnswerDislikesAdmin(admin.ModelAdmin):
    list_display = ('questionId', 'userId')
