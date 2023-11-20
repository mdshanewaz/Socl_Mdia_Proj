from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from Login_App.models import FollowerModel

# Create your views here.

@login_required
def home(request):
    following_list = FollowerModel.objects.filter(following=request.user)
    if request.method == 'GET':
        search = request.GET.get('search', '')
        result = User.objects.filter(username__icontains = search)


    return render(request, 'Posts_App/home.html', context={'title':'Home', 'search':search, 'result':result, 'following_list':following_list})