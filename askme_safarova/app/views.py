from django.core.paginator import Paginator
from django.shortcuts import render

from app.models import *

from app.models import Question

from app.models import Answer

QUESTIONS = Question.objects.all()
# QUESTIONS = [{"id": 0, "text": "", "title": ""}]
ANSWERS = Answer.objects.all()


def paginate(objects_list, request, per_page=5):
    page_num = request.GET.get('page', 1)
    paginator = Paginator(objects_list, per_page)
    page = paginator.page(page_num)
    return page


def index(request):
    return render(request, template_name='index.html', context={
        'questions': paginate(QUESTIONS, request, 5).object_list,
        'page_obj': paginate(QUESTIONS, request, 5),
    })


def hot(request):
    hot_q = Question.objects.best_question()[::-1]
    return render(request, template_name='hot.html', context={
        'questions': paginate(hot_q, request, 5).object_list,
        'page_obj': paginate(hot_q, request, 5)
    })


def question(request, question_id):
    one_question = ANSWERS
    # print(one_question)
    return render(request, template_name='question.html', context={
        'item': question_id,
        'questions': paginate(one_question, request, 1).object_list,
        'page_obj': paginate(one_question, request, 1),
    })


def signup(request):
    return render(request, template_name='signup.html', context={})


def login(request):
    return render(request, template_name='login.html', context={})


def ask(request):
    return render(request, template_name='ask.html', context={})


def tag(request, tag_name):
    list_of_tags = []
    for i in QUESTIONS:
        if tag_name in i["title"]:
            list_of_tags.append(i)
    return render(request, template_name='tag.html', context={
        'item': tag_name,
        'items': paginate(list_of_tags, request, 5).object_list,
        'page_obj': paginate(list_of_tags, request, 5)
    })