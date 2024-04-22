from django.shortcuts import redirect, render, HttpResponse
from django.shortcuts import render, get_object_or_404

from .forms import PostQuestionForm, RegistrationForm
from .models import Answer, Question, Comment, User, QuestionTag
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.db.models import Q


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


def post_question(request):
    if request.method == 'POST':
        form = PostQuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('some_view_name')
    else:
        form = PostQuestionForm()
    return render(request, 'questions/post_question.html', {'form': form})

def post_answer(request):
    if request.method == 'POST':
        form = PostAnswerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('some_view_name')
    else:
        form = PostAnswerForm()
    return render(request, 'questions/post_answer.html', {'form': form})

def post_comment(request):
    if request.method == 'POST':
        form = PostCommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('some_view_name')
    else:
        form = PostCommentForm()
    return render(request, 'questions/post_comment.html', {'form': form})

def search_question(request):
    if 'query' in request.GET:
        query = request.GET['query']
        questions = Question.objects.only('id', 'title').filter(title__icontains=query)
        return render(request, 'search_q_result.html', {'questions': questions})
    
def search_user(request):
    if 'query' in request.GET:
        query = request.GET['query']
        questions = User.objects.only('name', 'surname').filter(Q(name__icontains=query) | Q(surname__icontains=query))
        return render(request, 'search_u_result.html', {'questions': questions})

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