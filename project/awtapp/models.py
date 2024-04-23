from django.db import models
from django.forms import IntegerField
from django.utils import timezone

class User(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    hashedPassword = models.CharField(max_length=100)
    joinDate = models.DateField()
    admin = models.BooleanField(default=False)

class Question(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    postDate = models.DateTimeField(default=timezone.now)
    closed = models.BooleanField(default=False)
    views = models.IntegerField(default=0)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)

class Answer(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    questionId = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    postDate = models.DateTimeField(default=timezone.now)
    views = models.IntegerField(default=0)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)

class Comment(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    questionId = models.ForeignKey(Question, on_delete=models.CASCADE)
    answerId = models.ForeignKey(Answer, on_delete=models.CASCADE)
    content = models.TextField()
    postDate = models.DateTimeField(default=timezone.now)
    views = models.IntegerField(default=0)

class QuestionTag(models.Model):
    tag = models.CharField(max_length=100)
    questionId = models.ForeignKey(Question, on_delete=models.CASCADE)

class QuestionLikes(models.Model):
    questionId = models.ForeignKey(Question, on_delete=models.CASCADE)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['questionId', 'userId'], name='unique_key_pair_ql')
        ]


class QuestionDislikes(models.Model):
    questionId = models.ForeignKey(Question, on_delete=models.CASCADE)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['questionId', 'userId'], name='unique_key_pair_qd')
        ]


class AnswerLikes(models.Model):
    questionId = models.ForeignKey(Answer, on_delete=models.CASCADE)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['questionId', 'userId'], name='unique_key_pair_al')
        ]


class AnswerDislikes(models.Model):
    questionId = models.ForeignKey(Answer, on_delete=models.CASCADE)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['questionId', 'userId'], name='unique_key_pair_ad')
        ]
