from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib.auth.decorators import login_required


# @login_required
def home(request):
    context={
        'title': 'Home',
    }
    return render(request, 'posts/home.html', context=context)