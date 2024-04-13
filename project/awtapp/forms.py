from django import forms
from .models import Question

class AskQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['user', 'title', 'content']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(AskQuestionForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['user'].initial = user