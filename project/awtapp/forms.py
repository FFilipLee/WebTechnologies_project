from django import forms
from .models import Question, User
from django.utils import timezone

class AskQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'content']

    def __init__(self, *args, **kwargs):
        super(AskQuestionForm, self).__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.all()
        #self.fields['user'].label_from_instance = lambda obj: "%s" % obj.get_full_name()  # Customize this as per your User model

    # If you want to customize the save method to ensure some fields are automatically set
    def save(self, commit=True):
        instance = super(AskQuestionForm, self).save(commit=False)
        if not instance.pk:  # If this is a new instance, set postDate
            instance.postDate = timezone.now()
            instance.user = self.fields['user']
        if commit:
            instance.save()
            self.save_m2m()  # Required if the form has many-to-many relations
        return instance
    