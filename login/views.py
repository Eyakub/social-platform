from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import UserProfile
from .forms import CreateNewUser, EditProfile
from post.forms import PostForm
from login.models import Follow


def sign_up(request):
    form = CreateNewUser()
    registered = False
    if request.method == 'POST':
        form = CreateNewUser(data=request.POST)
        if form.is_valid():
            user = form.save()
            registered = True
            user_profile = UserProfile(user=user)
            user_profile.save()
            return HttpResponseRedirect(reverse('login:login'))
    context = {
        'title': 'Sign Up',
        'form': form
    }
    return render(request, 'login/signup.html', context=context)


def login_page(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('posts:home'))
    context = {
        'title': 'Login',
        'form': form,
    }
    return render(request, 'login/login.html', context=context)


@login_required
def edit_profile(request):
    current_user = UserProfile.objects.get(user=request.user)
    form = EditProfile(instance=current_user)

    if request.method == 'POST':
        form = EditProfile(request.POST, request.FILES, instance=current_user)
        if form.is_valid():
            form.save(commit=True)
            form = EditProfile(instance=current_user)
            return HttpResponseRedirect(reverse('login:profile'))
    context={
        'form': form,
        'title': 'Edit Profile'
    }
    return render(request, 'login/profile.html', context=context)


@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login:login'))


@login_required
def profile(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect(reverse('home'))
    context = {
        'title': 'User',
        'form': form
    }
    return render(request, 'login/user.html', context=context)


@login_required
def user(request, username):
    user = User.objects.get(username=username)
    already_followed = Follow.objects.filter(follower=request.user, following=user)
    if user == request.user:
        return HttpResponseRedirect(reverse('login:profile'))
    context = {
        'title': 'Profile',
        'user_other': user,
        'already_followed': already_followed,
    }
    return render(request, 'login/user_other.html', context=context)


@login_required
def follow(request, username):
    following_user = User.objects.get(username=username)
    follower_user = request.user
    already_followed = Follow.objects.filter(follower=follower_user, following=following_user)
    if not already_followed:
        followed_user = Follow(follower=follower_user, following=following_user)
        followed_user.save()
    return HttpResponseRedirect(reverse('login:user', kwargs={'username':username}))


@login_required
def unfollow(request, username):
    following_user = User.objects.get(username=username)
    follower_user = request.user
    already_followed = Follow.objects.filter(follower=follower_user, following=following_user)
    already_followed.delete()
    return HttpResponseRedirect(reverse('login:user', kwargs={'username': username}))