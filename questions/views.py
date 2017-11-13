# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render


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


def index(request):
    qlist = list()
    tags = lorem.words(5)
    for i in range(1, 5):
        shuffle(tags)
        qlist.append({
            'idx': i,
            'title': ' '.join(lorem.words(3)),
            'text': lorem.sentence(3),
            'tags': tags[0:3],
            'likes': randint(0, 20)
        })
    ctx['questions'] = qlist
    return render(request, 'index.html', ctx)


def login(request):
    return render(request, 'login.html', ctx)


def register(request):
    return render(request, 'register.html', ctx)


def settings(request):
    return render(request, 'settings.html', ctx)


def ask(request):
    return render(request, 'ask.html', ctx)


def oneQuestion(request):
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
