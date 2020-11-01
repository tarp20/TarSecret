from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Group
from django.views.generic import CreateView
from users.forms import CreationForm, PostForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


# Create your views here.

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


def group_post(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()
    paginator = Paginator(posts,5)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    
    contex = {'group': group, 'page':page,'paginator':paginator}
    return render(request, "group.html", contex)


class PostNew(CreateView):
    form_class = PostForm
    success_url = '/'
    template_name = 'new_post.html'


@login_required()
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
