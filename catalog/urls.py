from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import (ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView,
                           ProductDeleteView, ContactsTemplateView, BlogCreateView, BlogUpdateView,
                           BlogListView, BlogDetailView, BlogDeleteView)

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/create', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/update', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete', ProductDeleteView.as_view(), name='product_delete'),
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blog/create', BlogCreateView.as_view(), name='blog_create'),
    path('blog/<int:pk>/update', BlogUpdateView.as_view(), name='blog_update'),
    path('blog/<int:pk>/delete', BlogDeleteView.as_view(), name='blog_delete')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
