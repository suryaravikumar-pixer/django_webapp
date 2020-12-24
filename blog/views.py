from django.shortcuts import render ##default one
from .models import Post
# from django.http import HttpResponse #created



def home(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})
