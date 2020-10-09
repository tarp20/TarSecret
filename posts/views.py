from django.shortcuts import render,get_object_or_404,redirect
from .models import Post,Group
from django.views.generic import CreateView
from users.forms import CreationForm,PostForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    latest = Post.objects.order_by('-pub_date')[:11]
    return render(request,'index.html',{'posts':latest})

def group_post(request,slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:12]
    contex = {'group' : group, 'posts': posts}
    return render(request, "group.html", contex)

class PostNew(CreateView):
    form_class = CreationForm
    success_url = 'new_post'
    template_name = 'new_post.html'

@login_required()
def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            PostForm.save()
            return redirect('index')
        contex = {'form':form, 'author':Post.author}
        return render(request,'new_post.html',contex)

    form = PostForm()
    return render(request,'new_post.html',{'form':form})









