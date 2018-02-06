#!/usr/bin/env python
#---coding:utf-8---
#__auther__:Administrator
# date : 2018/2/1
from django import template
from ..models import Post,Category
from django.db.models.aggregates import Count

register = template.Library()

@register.simple_tag
def get_recent_posts(num=5):  # 获取最新的文章列表
    return Post.objects.all().order_by('-created_time')[:num]

@register.simple_tag
def archives():   # 定义归档模板标签
    return Post.objects.dates('created_time', 'month', order='DESC')


@register.simple_tag
def get_categories():   # 文章分类标签
    # 别忘了在顶部引入 Category 类
    return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)
