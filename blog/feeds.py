#!/usr/bin/env python
#---coding:utf-8---
#__auther__:Administrator
# date : 2018/2/6
from django.contrib.syndication.views import Feed
from .models import Post

class AllPostRssFeed(Feed):
    title = '我的博客' # 在RSS上显示的标题
    link = '/'
    # 显示在聚合阅读器上的描述信息
    description = "我的博文"

    # 需要显示的内容条目
    def items(self):
        return Post.objects.all()
    def item_title(self, item):
        return '[%s] %s' % (item.category, item.title)

    # 聚合器中显示的内容条目的描述
    def item_description(self, item):
        return item.body

