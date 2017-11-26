# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from questions.models import Question, Answer, Tag, Like

admin.site.register(Answer)
admin.site.register(Question)
admin.site.register(Tag)
admin.site.register(Like)

