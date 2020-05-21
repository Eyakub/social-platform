from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from login.models import UserProfile

# @login_required
def home(request):
    if request.method == 'GET':
        search = request.GET.get('search', '')
        result = User.objects.filter(username__icontains=search)
    context={
        'title': 'Home',
        'search': search,
        'result': result,
    }
    return render(request, 'posts/home.html', context=context)