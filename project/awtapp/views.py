from django.shortcuts import redirect, render, HttpResponse
from django.shortcuts import render, get_object_or_404

from .forms import AskQuestionForm, RegistrationForm
from .models import Answer, Question, Comment
from django.contrib.auth import authenticate, login, logout

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

def sign_up(request):
    print("view")
    if request.method == 'POST':
        print("post")
        form = RegistrationForm(request.POST)
        if form.is_valid():
            print("valid")
            user = form.save()
            login(request, user)
            return redirect('/search')
    else:
        print("get")
        form = RegistrationForm()
        context = {}
        context['form'] = form
        return render(request, 'sign_up.html', context)