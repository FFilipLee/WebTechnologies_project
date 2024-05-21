from django.contrib import admin
from .models import Question, Answer, Comment, QuestionTag, QuestionLike, QuestionDislike, AnswerLike, AnswerDislike

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'title', 'postDate', 'closed', 'views')

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'question', 'content', 'postDate', 'views')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'answer_id', 'content', 'postDate', 'views')

@admin.register(QuestionTag)
class QuestionTagAdmin(admin.ModelAdmin):
    list_display = ('tag', 'question')

@admin.register(QuestionLike)
class QuestionLikeAdmin(admin.ModelAdmin):
    list_display = ('question', 'user_id')

@admin.register(QuestionDislike)
class QuestionDislikeAdmin(admin.ModelAdmin):
    list_display = ('question', 'user_id')

@admin.register(AnswerLike)
class AnswerLikeAdmin(admin.ModelAdmin):
    list_display = ('answer', 'user_id')

@admin.register(AnswerDislike)
class AnswerDislikeAdmin(admin.ModelAdmin):
    list_display = ('answer', 'user_id')

