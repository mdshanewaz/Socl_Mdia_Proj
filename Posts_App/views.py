from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from Login_App.models import FollowerModel
from Posts_App.models import PostModel

# Create your views here.

@login_required
def home(request):
    following_list = FollowerModel.objects.filter(follower=request.user)
    posts = PostModel.objects.filter(author__in = following_list.values_list('following'))
    if request.method == 'GET':
        search = request.GET.get('search', '')
        result = User.objects.filter(username__icontains = search)


    return render(request, 'Posts_App/home.html', context={'title':'Home', 'search':search, 'result':result, 'posts':posts})