from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from product.serializers import CategorySerializers, ProductSerializers, ReviewSerializers
from product.models import Category, Product, Review


@api_view(['GET'])
def category_list_api_view(request):
    movies = Category.objects.all()
    data_dict = CategorySerializers(movies, many=True).data
    return Response(data=data_dict)


@api_view(['GET'])
def product_list_api_view(request):
    movies = Product.objects.all()
    data_dict = ProductSerializers(movies, many=True).data
    return Response(data=data_dict)


@api_view(['GET'])
def review_list_api_view(request):
    movies = Review.objects.all()
    data_dict = ReviewSerializers(movies, many=True).data
    return Response(data=data_dict)


@api_view(['GET'])
def category_detail_api_view(request, id):
    try:
        movie = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(data={'errors': 'Category not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    data_dict = CategorySerializers(movie, many=False).data
    return Response(data=data_dict)


@api_view(['GET'])
def product_detail_api_view(request, id):
    try:
        movie = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(data={'errors': 'Product not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    data_dict = ProductSerializers(movie, many=False).data
    return Response(data=data_dict)


@api_view(['GET'])
def review_detail_api_view(request, id):
    try:
        movie = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'errors': 'Review not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    data_dict = ReviewSerializers(movie, many=False).data
    return Response(data=data_dict)
