from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Search 
from django.db.models import Q

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/blog.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/blog.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

# function of search
def search(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        post = Search.objects.all().filter(title=search)
        return render(request, 'blog/search.html', {'posts':post} )
    #else: 
    #    return render(request, 'blog/search.html')

# trading page view
def trading(request):
    return render(request, 'blog/trading.html', {'title':'Trading'})

# data page view
def data(request):
    return render(request, 'blog/data.html', {'title':'Data'})  

# paper_research page view
def paper_research(request):
    return render(request, 'blog/paper_research.html', {'title':'Paper research'})   

# contact page view
def contact(request):
    return render(request, 'blog/contact.html', {'title':'Contact'})    

# about page view
def about(request): 
    return render(request, 'blog/about.html', {'title':'About'})    