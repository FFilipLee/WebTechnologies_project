from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    hashedPassword = models.CharField(max_length=100)
    joinDate = models.DateField()
    admin = models.BooleanField(default=False)

class Question(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=255)
    content = models.TextField()
    postDate = models.DateTimeField(default=timezone.now)
    closed = models.BooleanField(default=False)
    views = models.IntegerField(default=0)

class Answer(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    postDate = models.DateTimeField(default=timezone.now)
    views = models.IntegerField(default=0)

class Comment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    answer_id = models.ForeignKey(Answer, on_delete=models.CASCADE)
    content = models.TextField()
    postDate = models.DateTimeField(default=timezone.now)
    views = models.IntegerField(default=0)

class QuestionTag(models.Model):
    tag = models.CharField(max_length=100)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)

class QuestionLike(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['question_id', 'user_id'], name='unique_key_pair_ql')
        ]


class QuestionDislike(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['question_id', 'user_id'], name='unique_key_pair_qd')
        ]


class AnswerLike(models.Model):
    question_id = models.ForeignKey(Answer, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['question_id', 'user_id'], name='unique_key_pair_al')
        ]


class AnswerDislike(models.Model):
    question_id = models.ForeignKey(Answer, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['question_id', 'user_id'], name='unique_key_pair_ad')
        ]
