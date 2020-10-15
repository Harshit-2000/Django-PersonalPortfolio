from django.shortcuts import render, get_object_or_404
from .models import Blogs
# Create your views here.

def all_blog(request):
    blogs = Blogs.objects.all()
    return render(request, 'all_blogs.html', {'blogs' : blogs})

def details(request, blog_id):
    detail = get_object_or_404(Blogs, pk=blog_id)
    return render(request, 'details.html', {'details':detail})