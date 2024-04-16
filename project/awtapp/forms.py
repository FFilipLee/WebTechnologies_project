from django import forms
from .models import Question, User
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class AskQuestionForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.all(), label="Select User")

    class Meta:
        model = Question
        fields = ['user', 'title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter your question title here'}),
            'content': forms.Textarea(attrs={'placeholder': 'Write your question details here'}),
        }
    