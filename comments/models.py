#!/usr/bin/env python
#---coding:utf-8---
#__auther__:Administrator
# date : 2018/2/1
from django.db import models
from django.utils.six import python_2_unicode_compatible

@python_2_unicode_compatible
class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    url = models.URLField(blank=True)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    post = models.ForeignKey('blog.Post')

    def __str__(self):
        return self.text[:20]