# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render

from django.core.paginator import Paginator
from faker import lorem
from random import shuffle
from random import randint


ctx = dict()

members = dict({
    'text': 'Best members!',
    'people': ['First man', 'Second one', 'Last one']
})
ctx['members'] = members

tags = dict({
    'text': 'Popular tags',
    'tags': ['python', 'park', 'django']
})
ctx['tags'] = tags

# qlist = list()
# tags = lorem.words(5)
# range_size = 22
#
# if range_size < page_number:
#     page_number = 1
#
# questions_on_page = 4
# for i in range(1, range_size):
#     shuffle(tags)
#     qlist.append({
#         'idx': i,
#         'title': ' '.join(lorem.words(3)),
#         'text': lorem.sentence(3) + " id = " + str(i),
#         'tags': tags[0:3],
#         'likes': randint(0, 20),
#         'rightFlag': i % questions_on_page
#     })
# ctx['questions'] = qlist
#
# all_pages = qlist
# current_page = Paginator(all_pages, questions_on_page)
# ctx['pages'] = current_page.page(page_number)


def index(request, page_number=1):
    qlist = list()
    range_size = 22
    questions_on_page = 4

    tags = lorem.words(5)
    for i in range(1, range_size):
        shuffle(tags)
        qlist.append({
            'idx': i,
            'title': ' '.join(lorem.words(3)),
            'text': lorem.sentence(3) + " id = " + str(i),
            'tags': tags[0:3],
            'likes': randint(0, 20),
            'rightFlag': i % questions_on_page
        })
    ctx['questions'] = qlist

    all_pages = qlist
    current_page = Paginator(all_pages, questions_on_page)
    ctx['pages'] = current_page.page(page_number)
    return render(request, 'index.html', ctx)


def login(request):
    return render(request, 'login.html', ctx)


def register(request):
    return render(request, 'register.html', ctx)


def settings(request):
    return render(request, 'settings.html', ctx)


def ask(request):
    return render(request, 'ask.html', ctx)


def oneQuestion(request, number):
    questiontags = lorem.words(3)
    shuffle(questiontags)
    question = {
        'idx': 3,
        'title': ' '.join(lorem.words(3)),
        'text': lorem.sentence(3),
        'tags': questiontags[0:3],
    }
    ctx['question'] = question
    answerlist = list()
    for i in range(1, 5):
        answerlist.append({
            'idx': i,
            'title': ' '.join(lorem.words(3)),
            'text': lorem.sentence(18),
            'likes': randint(0, 20)
        })
    ctx['answers'] = answerlist

    return render(request, 'onequestion.html', ctx)
