from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import ProductForm
from .models import Product
# Create your views here.

@login_required
def product_create_view(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            instance.user = request.user
            # print(request.FILES['image'])
            # print(form.instance)
            # print(form)
            instance.save()
            return redirect('post_create_view')
    return render(request, 'products/partials/product_create_view.html', {'form': form})



class MyProductsListView(ListView):
    model = Product
    context_object_name = 'my_products'
    template_name = 'products/my_products.html'

    def get_queryset(self, *args, **kwargs):
        qs = Product.objects.filter(user=self.request.user)
        qs.order_by("-created_at")
        return qs


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/partials/product_details.html'



class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/partials/product_create_view.html'
    success_url = '/'

    def form_valid(self, form):
        if self.object.user == self.request.user:
            return super().form_valid(form)
        else:
            return redirect('list_view')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'posts/partials/delete_view.html'
    success_url = '/'
    def form_valid(self, form):
        if self.object.user == self.request.user:
            return super().form_valid(form)
        else:
            return HttpResponse('Don`t be rude!')