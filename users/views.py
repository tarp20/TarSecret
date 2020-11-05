from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CreationForm,ContactForm,PostForm,FollowForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Follow,User
from posts.models import Post
from django.core.paginator import Paginator



class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"


def user_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return redirect('/thank-you/')
            return render(request, 'contact.html', {'form': form})

    form = ContactForm()
    return render(request, 'contact.html', {'form': form})

@login_required(login_url="/auth/login/")
def follow_index(request):
    follows = User.objects.get(pk=request.user.id).follower.all().values_list('author')
    posts = Post.objects.filter(author__in = follows)
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {'page':page,'paginator':paginator}
    return render(request, "post/follow.html", context)

@login_required(login_url="/auth/login/")
def profile_follow(request, username):
    user = get_object_or_404(User,username=username)
    follower = Follow.objects.create(user=request.user,author=user)
    follower.save()
    return redirect('profile', username=username)


@login_required(login_url="/auth/login/")
def profile_unfollow(request, username):
    user = get_object_or_404(User, username=username)
    follower = Follow.objects.get(user=request.user,author=user)
    follower.delete()
    return redirect('index')




    






