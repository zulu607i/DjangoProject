from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_post', views.post_create_view , name='post_create_view'),
    path('all_posts', views.AllPostsListView.as_view(), name='list_view'),
    path('my_posts', views.MyPostsListView.as_view(), name='my_posts_view'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='detail_view'),
    path('update/<int:pk>/', views.PostUpdateView.as_view(), name='post_update'),
    path('delete/<int:pk>/', views.DeletePostView.as_view(), name='post_delete'),

]