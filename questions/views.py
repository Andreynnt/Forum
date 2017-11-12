# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render


from faker import lorem
from random import shuffle


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
        })
    ctx['questions'] = qlist
    print(ctx['members'])
    return render(request, 'index.html', ctx)


def login(request):
    return render(request, 'login.html', ctx)
