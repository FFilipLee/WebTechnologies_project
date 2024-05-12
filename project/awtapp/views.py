from pprint import pprint
from django.shortcuts import redirect, render, HttpResponse
from django.shortcuts import render, get_object_or_404
from .forms import PostQuestionForm, PostAnswerForm, PostCommentForm, SignupForm, LoginForm
from .models import Answer, Question, Comment, User, QuestionLike, QuestionDislike, AnswerLike, AnswerDislike
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
    answers = Answer.objects.filter(question=question)
    answer_comments = {}
    for answer in answers:
        answer_comments[answer] = Comment.objects.filter(answer=answer)
    pprint(answer_comments)
    return render(request, 'questions/question_detail.html', {'question': question, 'answers': answers, 'answer_comments': answer_comments})

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

@login_required
def question_like(request, question_id):
    if Question.objects.filter(id=question_id).exists():
        if not QuestionLike.objects.filter(user_id=request.user.id, question_id=question_id).exists():
            QuestionLike(user_id=request.user.id, question_id=question_id).save()
            return HttpResponse("Question liked.", status=200)
        else:
            QuestionLike(user_id=request.user.id, question_id=question_id).delete()
            return HttpResponse("Question unliked.", status=200)
    return HttpResponse("Such question does not exist.", status=404)

@login_required
def question_dislike(request, question_id):
    if Question.objects.filter(id=question_id).exists():
        if not QuestionDislike.objects.filter(user_id=request.user.id, question_id=question_id).exists():
            QuestionDislike(user_id=request.user.id, question_id=question_id).save()
            return HttpResponse("Question disliked.", status=200)
        else:
            QuestionDislike(user_id=request.user.id, question_id=question_id).delete()
            return HttpResponse("Question undisliked.", status=200)
    return HttpResponse("Such question does not exist.", status=404)
    
@login_required
def answer_like(request, answer_id):
    if Question.objects.filter(id=answer_id).exists():
        if not AnswerLike.objects.filter(user_id=request.user.id, answer_id=answer_id).exists():
            AnswerLike(user_id=request.user.id, answer_id=answer_id).save()
            return HttpResponse("Answer liked.", status=200)
        else:
            AnswerLike(user_id=request.user.id, answer_id=answer_id).delete()
            return HttpResponse("Answer unliked.", status=200)
    return HttpResponse("Such answer does not exist.", status=404)

@login_required
def answer_dislike(request, answer_id):
    if Question.objects.filter(id=answer_id).exists():
        if not AnswerDislike.objects.filter(user_id=request.user.id, answer_id=answer_id).exists():
            AnswerDislike(user_id=request.user.id, answer_id=answer_id).save()
            return HttpResponse("Answer disliked.", status=200)
        else:
            AnswerDislike(user_id=request.user.id, answer_id=answer_id).delete()
            return HttpResponse("Answer undisliked.", status=200)
    return HttpResponse("Such answer does not exist.", status=404)