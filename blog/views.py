from django.shortcuts import render,get_object_or_404
import markdown
from comments.forms import CommentForm


# Create your views here.
from django.http import HttpResponse
from .models import Post,Category

def index(request,*args):
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', context={ 'post_list':post_list })

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(
        post.body,extensions=[ 'markdown.extensions.extra',
                               'markdown.extensions.codehilite',
                               'markdown.extensions.toc',
                                  ])
    form = CommentForm()
    comment_list = post.comment_set.all()
    # 将文章、表单、以及文章下的评论列表作为模板变量传给 detail.html 模板，以便渲染相应数据。
    context = {'post':post,
               'form':form,
               'comment_list':comment_list}
    return render(request, 'blog/detail.html', context=context)

def archives(request, year, month):
    post_list = Post.objects.filter(
        created_time__year=year,
        created_time__month=month
    )
    return render(request, 'blog/index.html', context={'post_list': post_list})



