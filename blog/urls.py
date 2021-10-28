from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView #PostCommentView
from . import views

urlpatterns = [
    path('blog', PostListView.as_view(), name='blog-blog'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),

    #my recently added pages view
    path('search/', views.search, name='blog-search'),
    path('', views.trading, name='blog-trading'),
    path('paper_research/', views.paper_research, name='blog-paper_research'),
    path('data/', views.data, name='blog-data'),
    # path('post/<int:pk>/comment/', PostCommentView.as_view(), name='post-comment'),
    path('contact/', views.contact, name='blog-contact'),
    path('about/', views.about, name='blog-about'),
]
