from unicodedata import category
from django import template
from blog.models import Post,Comment
from django.utils import timezone
from blog.models import Category
from bs4 import BeautifulSoup
from django.shortcuts import render,get_object_or_404


register = template.Library()

@register.simple_tag(name='totalpost')
def plus():
    posts= Post.objects.filter(status = 1)
    return posts

@register.simple_tag(name='comments_count')
def function(pid):
    
    return Comment.objects.filter(post=pid,approved=True).count()



@register.filter
def snipet(value,arg=20):
    soup = BeautifulSoup(value, features="html.parser")
    
    return soup.get_text()[0:arg]+'...'


@register.inclusion_tag('blog/blog-single-recentpost.html')
def latestposts(arg=2):
    posts= Post.objects.filter(status = 1,published_date__lte=timezone.now()).order_by('-published_date')[:arg]
    return {'posts': posts}

@register.inclusion_tag('blog/blog-single-category.html')
def postcategories():
    cat_dict={}
    posts = Post.objects.filter(status=1)
    categories= Category.objects.all()
    for name in categories:
        cat_dict[name]=posts.filter(category=name).count()
       
    return {'categories': cat_dict}

@register.inclusion_tag('blog/blog-latest-posts.html')
def latest_posts(arg=6):
    posts= Post.objects.filter(status = 1,published_date__lte=timezone.now()).order_by('-published_date')[:arg]
    return {'posts': posts}

@register.inclusion_tag('blog/blog-next-prev.html')
def nextprev_posts(pid=6):
    posts = Post.objects.filter(status = 1,published_date__lte=timezone.now()).order_by('-published_date')
    postn= get_object_or_404(posts, pk=pid)
    return {'postn': postn}