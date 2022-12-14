from django.shortcuts import render, get_object_or_404
from .models import Blog


# Create your views here.
def all_blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/all_blogs.html', {'tittle': 'Blog', 'blog': blogs})


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'tittle': f'Blog #{blog_id}', 'blog': blog})
