from django.shortcuts import redirect, render, HttpResponse
from django.shortcuts import render, get_object_or_404

from .forms import PostQuestionForm, PostAnswerForm, PostCommentForm
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
        form = PostQuestionForm(request.user, request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            return redirect('some_view_name')
    else:
        form = PostQuestionForm(request.user)  
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
    
def delete_question(request):
    if 'query' in request.GET:
        query = request.GET['query']
        if Question.objects.filter(id=query).exists():
            Question.objects.filter(id=query).delete()
        return render(request, 'home.html', {})

def delete_answer(request):
    if 'query' in request.GET:
        query = request.GET['query']
        if Answer.objects.filter(id=query).exists():
            Answer.objects.filter(id=query).delete()
        return render(request, 'home.html', {})

def delete_comment(request):
    if 'query' in request.GET:
        query = request.GET['query']
        if Comment.objects.filter(id=query).exists():
            Comment.objects.filter(id=query).delete()
        return render(request, 'home.html', {})
    
def search_user(request):
    if 'query' in request.GET:
        query = request.GET['query']
        questions = User.objects.only('name', 'surname').filter(Q(name__icontains=query) | Q(surname__icontains=query))
        return render(request, 'search_u_result.html', {'questions': questions})
    
def delete_user(request):
    if 'query' in request.GET:
        query = request.GET['query']
        if User.objects.filter(id=query).exists():
            User.objects.filter(id=query).delete()
        return render(request, 'home.html', {})

def home(request):
    questions = Question.objects.all()
    return render(request, 'home/home.html', {'questions': questions})

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import SignupForm, LoginForm

def index(request):
    return render(request, 'index.html')

def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')