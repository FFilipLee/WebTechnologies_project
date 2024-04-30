from django.contrib import admin
from .models import  Question, Answer, Comment, QuestionTag, QuestionLike, QuestionDislike, AnswerLike, AnswerDislike


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'postDate', 'closed', 'views', 'upvotes', 'downvotes')

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'question', 'content', 'postDate', 'views', 'upvotes', 'downvotes')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'question', 'answer', 'content', 'postDate', 'views')

@admin.register(QuestionTag)
class QuestionTagAdmin(admin.ModelAdmin):
    list_display = ('tag', 'question')

@admin.register(QuestionLike)
class QuestionLikeAdmin(admin.ModelAdmin):
    list_display = ('question', 'user')

@admin.register(QuestionDislike)
class QuestionDislikeAdmin(admin.ModelAdmin):
    list_display = ('question', 'user')

@admin.register(AnswerLike)
class AnswerLikeAdmin(admin.ModelAdmin):
    list_display = ('question', 'user')

@admin.register(AnswerDislike)
class AnswerDislikeAdmin(admin.ModelAdmin):
    list_display = ('question', 'user')
