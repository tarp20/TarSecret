from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Group, User
from django.views.generic import CreateView
from users.forms import CreationForm, PostForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from django.http import HttpResponse


from django.http import HttpResponse


# Create your views here.
@login_required(login_url="/auth/login/")
def index(request):
    latest = Post.objects.order_by('-pub_date').all()
    paginator = Paginator(latest, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(
        request,
        'index.html',
        {'page': page, 'paginator': paginator}
    )


@login_required(login_url="/auth/login/")
def group_post(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    contex = {'group': group, 'page':page,'paginator':paginator}
    return render(request, "group.html", contex)


@login_required(login_url="/auth/login/")
class PostNew(CreateView):
    form_class = PostForm
    success_url = '/'
    template_name = 'new_post.html'


@login_required(login_url="/auth/login/")
def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('index')
        return render(request, 'new_post.html', {"form": form})

    form = PostForm()
    return render(request, 'new_post.html', {'form': form})


@login_required(login_url="/auth/login/")
def profile(request, username):
    user = get_object_or_404(User, username=username)
    posts = user.posts.all()
    paginator = Paginator(posts,5)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    count = len(posts)
    context = {'page': page, 'user': user, 'count': count,'paginator':paginator}
    return render(request, 'profile.html', context)


@login_required(login_url="/auth/login/")
def post_view(request, username, post_id):
    user = get_object_or_404(User,username=username)
    post = get_object_or_404(Post,pk=post_id,author=user)
    count = len(user.posts.all())
    context = {'user':user,'post':post,'count':count}
    return render(request, 'post.html', context)


@login_required(login_url="/auth/login/")
def post_edit(request, username, post_id):

    profile = get_object_or_404(User, username=username)
    post = get_object_or_404(Post, pk=post_id, author=profile)
    if request.user != profile:
        return redirect('index')
    
    form = PostForm(request.POST or None, files=request.FILES or None, instance=post)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect("index")

    return render(
        request, 'post_edit.html', {'form': form, 'post': post},
    )


def page_not_found(request, exception):
    return render(
        request, 
        "mics/404.html", 
        {"path": request.path}, 
        status=404)

def server_error(request):
    return render(request, "mics/500.html", status=500)


    form = PostForm(instance =Post.objects.get(id =post_id))

    if username != request.user.username:
        HttpResponse("ERROR")

    if request.method == "POST":
        form = PostForm(request.POST, instance=Post.objects.get(id=post_id))
    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request, 'edit_post.html', {'form': form})

