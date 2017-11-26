# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


import os
from django.conf import settings

from django.utils import timezone
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User)


class QuestionManager(models.Manager):
    def best_questions(self):
        return self.filter(rating__gt=10).order_by('-rating')

    def new_questions(self):
        return self.order_by('-created_at')


class Question(models.Model):
    title = models.CharField(max_length=60)
    text = models.TextField()
    author = models.ForeignKey(Profile)
    rating = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    tags = models.ManyToManyField('Tag')

    objects = QuestionManager()

    def __unicode__(self):
        return u'{0} - {1}'.format(self.id, self.title)

    def get_url(self):
        return '/question{question_id}/'.format(question_id=self.id)

    def get_answers(self):
        return Answer.objects.filter(answer_question_id=self.id)


class Answer(models.Model):
    text = models.TextField()
    author = models.ForeignKey(Profile)
    created_at = models.DateTimeField(default=timezone.now)
    question = models.ForeignKey(Question)
    rating = models.IntegerField(default=0)

    # objects = AnswerManager()

    def get_url(self):
        return self.question.get_url()

    def __unicode__(self):
        return u'{0} - {1}'.format(self.id, self.text)


class Tag(models.Model):
    name = models.CharField(max_length=60)


class Like(models.Model):
    owner = models.ForeignKey(Profile)
    question_id = models.ForeignKey(Question, null=False)
    answer_id = models.ForeignKey(Answer, null=True)
    value = models.BooleanField()

    def __unicode__(self):
        return u'{0} - {1} - {2}'.format(self.question_id, self.answer_id, self.owner)
