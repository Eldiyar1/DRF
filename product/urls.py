from django.urls import path
from product.views import CategoryListCreateAPIView, CategoryDetailAPIView, ProductListCreateAPIView, \
    ProductDetailAPIView, ReviewListCreateAPIView, ReviewDetailAPIView

urlpatterns = [
    path('categorys/', CategoryListCreateAPIView.as_view()),
    path('categorys/<int:pk>/', CategoryDetailAPIView.as_view()),
    path('products/', ProductListCreateAPIView.as_view()),
    path('products/<int:pk>/', ProductDetailAPIView.as_view()),
    path('reviews/', ReviewListCreateAPIView.as_view()),
    path('reviews/<int:pk>/', ReviewDetailAPIView.as_view()),
]