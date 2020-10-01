from django.shortcuts import render,get_object_or_404
from .models import Post,Group


# Create your views here.

def index(request):
    latest = Post.objects.order_by('-pub_date')[:11]
    return render(request,'index.html',{'posts':latest})

def group_post(request,slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:12]
    contex = {'group' : group, 'posts': posts}
    return render(request, "group.html", contex)







