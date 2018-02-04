#!/usr/bin/env python
#---coding:utf-8---
#__auther__:Administrator
# date : 2018/2/2

from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text']