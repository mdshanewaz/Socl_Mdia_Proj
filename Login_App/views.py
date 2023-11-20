from django.shortcuts import render, HttpResponseRedirect
from Login_App.models import UserprofileModel, FollowerModel
from Login_App.forms import CreateUserForm, EditProfile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from Posts_App.forms import PostForm

# Create your views here.

def signup_view(request):
    form = CreateUserForm()
    registered = False

    if request.method == 'POST':
        form = CreateUserForm(data=request.POST)

        if form.is_valid():
            user = form.save()
            registered = True
            user_profile = UserprofileModel(user=user)
            user_profile.save()
            
            return HttpResponseRedirect(reverse('Login_App:login'))

    return render(request, 'Login_App/signup.html', context={'title':'SignUp', 'form':form, 'registered':registered})


def login_view(request):
    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(username=username, password=password)
            
            if user is  not None:
                login(request, user)
                return HttpResponseRedirect(reverse('Posts_App:home'))

    return render(request, 'Login_App/login.html', context={'title':'Login', 'form':form})


@login_required
def editprofile_view(request):
    current_user = UserprofileModel.objects.get(user=request.user)
    form = EditProfile(instance=current_user)

    if request.method == 'POST':
        form = EditProfile(request.POST, request.FILES, instance=current_user)
        
        if form.is_valid():
            form.save(commit=True)
            form = EditProfile(instance=current_user)
            return HttpResponseRedirect(reverse('Login_App:profile'))

    return render(request, 'Login_App/profile.html', context={'title':'Profile', 'form':form})


@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('Login_App:login'))


@login_required
def profile_view(request):
    form = PostForm
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid:
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect(reverse('Posts_App:home')) 
    return render(request, 'Login_App/user.html', context={'title':'Profile', 'form': form})

@login_required
def user_view(request, username):
    user_other = User.objects.get(username=username)
    already_followed = FollowerModel.objects.filter(follower=request.user, following=user_other)
    if user_other == request.user:
        return HttpResponseRedirect(reverse('Login_App:profile'))
    return render(request, 'Login_App/user_other.html', context={'user_other':user_other, 'title': username, 'already_followed':already_followed})

@login_required
def follow_view(request, username):
    following_user = User.objects.get(username=username)
    follower_user = request.user
    already_followed = FollowerModel.objects.filter(follower=follower_user, following=following_user)

    if not already_followed:
        followed_user = FollowerModel(follower=follower_user, following=following_user)
        followed_user.save()
    return HttpResponseRedirect(reverse('Login_App:user', kwargs={'username':username}))

@login_required
def unfollow_view(request, username):
    following_user = User.objects.get(username=username)
    follower_user = request.user
    already_followed = FollowerModel.objects.filter(follower=follower_user, following=following_user)
    already_followed.delete()
    return HttpResponseRedirect(reverse('Login_App:user', kwargs={'username':username}))