from django import forms
from .models import Question, User, Answer, Comment
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostQuestionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(PostQuestionForm, self).__init__(*args, **kwargs)
        self.user = user  # Store the user object
        if user:
            self.fields['user'].initial = user
            self.fields['user'].widget.attrs['readonly'] = True

    class Meta:
        model = Question
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter your question title here'}),
            'content': forms.Textarea(attrs={'placeholder': 'Write your question details here'}),
        }

class PostAnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': 'Write your answer here...'}),
        }

class PostCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': 'Write your answer here...'}),
        }

class SignupForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class SearchForm(forms.Form):
    query = forms.CharField(label='Search')

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']