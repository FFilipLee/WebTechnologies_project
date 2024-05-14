from pprint import pprint
from django.shortcuts import redirect, render, HttpResponse
from django.shortcuts import render, get_object_or_404

from .forms import LoginForm, PostQuestionForm, PostAnswerForm, PostCommentForm, SearchForm, SignupForm
from .models import Answer, Question, Comment, User, QuestionTag, QuestionLike, QuestionDislike, AnswerLike, AnswerDislike
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils import timezone


def question_list(request):
    questions = Question.objects.all()
    return render(request, 'questions/question_list.html', {'questions': questions})

def question_detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    question.views += 1
    answer_ids = Answer.objects.filter(question_id=question_id)
    answer_comments = {}
    for answer_id in answer_ids:
        answer_comments[answer_id] = Comment.objects.filter(answer_id=answer_id)
    pprint(answer_comments)
    return render(request, 'questions/question_detail.html', {'question': question, 'answers': answer_ids, 'answer_comments': answer_comments})

@login_required
def post_question(request):
    if request.method == 'POST':
        form = PostQuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            user_instance = User.objects.get(pk=request.user.pk)
            question.user = user_instance
            question.save()
            return redirect('home')
    else:
        form = PostQuestionForm()  
    return render(request, 'create_question.html', {'form': form})

@login_required
def post_answer(request, question_id):
    if request.method == 'POST':
        form = PostAnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user  
            answer.question_id = question_id  
            answer.postDate = timezone.now()  
            answer.save()
            return redirect('question_detail', pk=question_id)
    elif request.method == 'GET':
        form = PostAnswerForm()  
        return render(request, 'create_answer.html', {'form': form})
    return HttpResponse("Method not allowed.", status=405)


@login_required
def post_comment(request):
    if request.method == 'POST':
        form = PostCommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('some_view_name')
    elif request.method == 'GET':
        form = PostCommentForm()
        return render(request, 'questions/post_comment.html', {'form': form})
    return HttpResponse("Method not allowed.", status=405)

def search_question(request, query):
    if request.method == 'GET':
        questions = Question.objects.only('id', 'title').filter(title__icontains=query)
        return render(request, 'search_q_result.html', {'questions': questions})
    return HttpResponse("Method not allowed.", status=405)
    
@login_required
def delete_question(request, question_id):
    if request.method == 'GET':
        answer = get_object_or_404(Question, id=question_id)
        if answer.user_id == request.user.id or request.user.is_superuser:
            Question.objects.filter(id=question_id).delete()
            return render(request, 'home.html', {})
        return HttpResponse("No rights to delete this content.", status=403)
    return HttpResponse("Method not allowed.", status=405)

@login_required
def delete_answer(request, answer_id):
    if request.method == 'GET':
        answer = get_object_or_404(Answer, id=answer_id)
        if answer.user_id == request.user.id or request.user.is_superuser:
            Answer.objects.filter(id=answer_id).delete()
            return render(request, 'home.html', {})
        return HttpResponse("No rights to delete this content.", status=403)
    return HttpResponse("Method not allowed.", status=405)

@login_required
def delete_comment(request, comment_id):
    if request.method == 'GET':
        answer = get_object_or_404(Comment, id=comment_id)
        if answer.user_id == request.user.id or request.user.is_superuser:
            Comment.objects.filter(id=comment_id).delete()
            return render(request, 'home.html', {})
        return HttpResponse("No rights to delete this content.", status=403)
    return HttpResponse("Method not allowed.", status=405)
    
def search_user(request):
    if 'query' in request.GET:
        query = request.GET['query']
        questions = User.objects.only('name', 'surname').filter(Q(name__icontains=query) | Q(surname__icontains=query))
        return render(request, 'search_u_result.html', {'questions': questions})
    return HttpResponse("Method not allowed.", status=405)
    
@login_required
def delete_user(request, user_id):
    if request.method == 'GET':
        user = get_object_or_404(User, id=user_id)
        if user_id == request.user.id or request.user.is_superuser:
            User.objects.filter(id=user_id).delete()
            return render(request, 'home.html', {})
        return HttpResponse("No rights to delete this content.", status=403)            
    return HttpResponse("Method not allowed.", status=405)
    

def home(request):
    questions = Question.objects.all()
    return render(request, 'home/home.html', {'questions': questions})

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

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

def search(request):
    form = SearchForm(request.GET)
    results = []

    if form.is_valid():
        query = form.cleaned_data['query']
        results = Question.objects.filter(
            Q(title__icontains=query) | 
            Q(content__icontains=query)
        )

    return render(request, 'search_results.html', {'form': form, 'results': results})

def calculate_question_likes(request, question_id):
    if Question.objects.filter(id=question_id).exists():
        count = QuestionLike.objects.filter(question_id=question_id).count()
        return HttpResponse(count, status=200)
    return HttpResponse("No such question.", status=404)

def calculate_question_dislikes(request, question_id):
    if Question.objects.filter(id=question_id).exists():
        count = QuestionDislike.objects.filter(question_id=question_id).count()
        return HttpResponse(count, status=200)
    return HttpResponse("No such question.", status=404)

def calculate_answer_likes(request, answer_id):
    if Answer.objects.filter(id=answer_id).exists():
        count = AnswerLike.objects.filter(answer_id=answer_id).count()
        return HttpResponse(count, status=200)
    return HttpResponse("No such answer.", status=404)

def calculate_answer_dislikes(request, answer_id):
    if Answer.objects.filter(id=answer_id).exists():
        count = AnswerDislike.objects.filter(answer_id=answer_id).count()
        return HttpResponse(count, status=200)
    return HttpResponse("No such answer.", status=404)
