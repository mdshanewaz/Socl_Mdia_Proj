from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from Login_App.models import FollowerModel
from Posts_App.models import PostModel, LikeModel

# Create your views here.

@login_required
def home(request):
    following_list = FollowerModel.objects.filter(follower=request.user)
    posts = PostModel.objects.filter(author__in = following_list.values_list('following'))
    
    liked_post = LikeModel.objects.filter(user=request.user)
    liked_post_list = liked_post.values_list(flat=True)

    print(liked_post_list)

    if request.method == 'GET':
        search = request.GET.get('search', '')
        result = User.objects.filter(username__icontains = search)


    return render(request, 'Posts_App/home.html', context={'title':'Home', 'search':search, 'result':result, 'posts':posts, 'liked_post_list':liked_post_list})

@login_required
def liked_view(request, pk):
    post = PostModel.objects.get(pk=pk)
    already_liked = LikeModel.objects.filter(post=post, user=request.user)
    
    if not already_liked:
        liked_post = LikeModel(post=post, user=request.user)
        liked_post.save()

    return HttpResponseRedirect(reverse('Posts_App:home'))

@login_required
def unlike_view(request, pk):
    post = PostModel.objects.get(pk=pk)
    already_liked = LikeModel.objects.filter(post=post, user=request.user)
    already_liked.delete()
    return HttpResponseRedirect(reverse('Posts_App:home'))