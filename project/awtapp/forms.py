from django import forms
from .models import Question, User, Answer, Comment
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostQuestionForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.all(), label="Select User")

    class Meta:
        model = Question
        fields = ['user', 'title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter your question title here'}),
            'content': forms.Textarea(attrs={'placeholder': 'Write your question details here'}),
        }
    
class PostAnswerForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.all(), label="Select User")
    question = forms.ModelChoiceField(queryset=Question.objects.all(), label="Select Question")

    class Meta:
        model = Answer
        fields = ['user', 'question', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': 'Write your answer here'}),
        }

class PostCommentForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.all(), label="Select User")
    answer = forms.ModelChoiceField(queryset=Answer.objects.all(), label="Select Answer")

    class Meta:
        model = Comment
        fields = ['user', 'answer', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': 'Write your comment here'}),
        }


from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)