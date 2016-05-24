# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Todo(models.Model):
    STATUS_CHOICES = [
        (0, u'已完成'),
        (1, u'未完成'),
    ]
    content = models.CharField(max_length=50)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.content

    class Meta:
        ordering = ['-updated_at']

