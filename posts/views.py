from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.http import HttpResponse
from .forms import PostCreate
from .models import Post
# Create your views here.


def post_create_view(request):
    form = PostCreate(request.POST)
    if form.is_valid():
        instance = form.save()
        instance.user = request.user
        instance.save()

        return redirect('home')
    return render(request, 'partials/create_post_view.html', {'form': form})


class AllPostsListView(ListView):
    model = Post
    context_object_name = 'allposts'
    template_name = 'partials/list_row.html'

    def get_queryset(self):
        return Post.objects.order_by('-created_at')


class MyPostsListView(ListView):
    model = Post
    context_object_name = 'allposts'
    template_name = 'partials/list_row.html'

    def get_queryset(self, *args, **kwargs):
        qs = Post.objects.filter(user=self.request.user)
        qs.order_by("-created_at")
        return qs


class PostDetailView(DetailView):
    model = Post
    template_name = 'partials/post_detail.html'


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostCreate
    template_name = 'partials/update_view.html'
    success_url = '/all_posts'

    def form_valid(self, form):
        if self.object.user == self.request.user:
            return super().form_valid(form)
        else:
            return redirect('list_view')


class DeletePostView(DeleteView):
    model = Post
    template_name = 'partials/delete_view.html'

    def form_valid(self, form):
        if self.object.user == self.request.user:
            return super().form_valid(form)
        else:
            return HttpResponse('Don`t be rude!')










# def list_view(request):
#     context = {'allposts': Post.objects.all()}
#     return render(request, 'partials/list_row.html', context)
#
#
# def list_view_my_posts(request):
#     context = {'myposts': Post.objects.filter(user=request.user)}
#     return render(request, 'partials/list_row_my_posts.html', context)
