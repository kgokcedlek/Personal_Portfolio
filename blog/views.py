from django.shortcuts import render, get_object_or_404
from .models import Project_Blog

# Create your views here.

def all_blog(request):
    blogs = Project_Blog.objects.order_by('-date')[:5]
    return render(request,'blog/all_blog.html',{'blogs':blogs})

def details(request, blog_id):
    blog = get_object_or_404(Project_Blog, pk=blog_id)
    return render(request,'blog/details.html',{'blog':blog})
