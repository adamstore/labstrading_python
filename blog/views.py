from django.shortcuts import render

posts = [
    {
        'author':'karim',
        'title':'top 1',
        'content':'my first article 1',
        'date': ' may 15, 2000',
    },
    {
        'author':'me',
        'title':'top 2',
        'content':'my first article 2',
        'date': ' may 20, 2000',
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'about'})    