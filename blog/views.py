from django.shortcuts import render ##default one

# from django.http import HttpResponse #created

posts = [
    {
        'author': 'surya',
        'title':  'Blog post',
        'content': 'First Post content',
        'date_posted': 'December 24, 2020'
    },
     {
        'author': 'Jane Doe',
        'title':  'Blog post 2',
        'content': 'Second Post content',
        'date_posted': 'December 24, 2020'
    }
]

def home(request):
    context = {
        'posts':posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})
