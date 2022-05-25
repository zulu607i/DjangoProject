from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('create_product/', views.product_create_view, name='product_create'),
    path('/my_products', views.MyProductsListView.as_view(), name='my_products'),
    path('details/<int:pk>/', views.ProductDetailView.as_view(), name='product_details'),
    path('delete/<int:pk>/', views.ProductDeleteView.as_view(), name='product_delete'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)