from django.shortcuts import redirect, render, HttpResponse
from django.shortcuts import render, get_object_or_404

from .forms import AskQuestionForm
from .models import Answer, Question, Comment

def question_list(request):
    questions = Question.objects.all()
    return render(request, 'questions/question_list.html', {'questions': questions})

def question_detail(request, pk):
    question = get_object_or_404(Question, id=pk)
    answers = Answer.objects.filter(question=question)
    answer_comments = {}
    for answer in answers:
        answer_comments[answer] = Comment.objects.filter(answer=answer)
    return render(request, 'questions/question_detail.html', {'question': question, 'answers': answers, 'answer_comments': answer_comments})

def ask_question(request):
    if request.method == 'POST':
        form = AskQuestionForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            # Create a new question object
            question = Question.objects.create(title=title, content=content)
            return redirect('question_detail', id=question.pk)

    else:
        form = AskQuestionForm()
    return render(request, 'questions/ask_question.html', {'form': form})

def home(request):
    questions = Question.objects.all()
    return render(request, 'home/home.html', {'questions': questions})