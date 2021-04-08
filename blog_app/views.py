from django.shortcuts import render
import requests
from blog_app.models import Blog
from django.http import JsonResponse, HttpResponse, Http404, HttpResponseRedirect
import re
# Create your views here.


def blogs(request):
    blogs = Blog.objects.order_by('created_date_time')
    return render(request, 'blog_app/blogs.html', context={"blogs": blogs})


def getBlog(request, slug):
    blog = Blog.objects.get(slug=slug)
    return render(request, 'blog_app/post.html', context={"blog": blog})
