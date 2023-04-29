from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from product.serializers import CategorySerializers, ProductSerializers, ReviewSerializers
from product.models import Category, Product, Review


@api_view(['GET', 'POST'])
def product_list_api_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        data_dict = ProductSerializers(products, many=True).data
        return Response(data=data_dict)
    elif request.method == 'POST':
        """ READ BODY """
        title = request.data.get('title')
        description = request.data.get('description')
        price = request.data.get('price')
        product_id = request.data.get('product_id')
        """ CREATE PRODUCT """
        product = Product.objects.create(title=title, description=description, price=price,
                                         product_id=product_id)
        product.save()
        """ RETURN RESPONSE """
        return Response(data=ProductSerializers(product).data)


@api_view(['GET', 'POST'])
def category_list_api_view(request):
    if request.method == 'GET':
        category = Category.objects.all()
        data_dict = CategorySerializers(category, many=True).data
        return Response(data=data_dict)
    elif request.method == 'POST':
        """ READ BODY """
        name = request.data.get('name')
        """ CREATE CATEGORY """
        category = Category.objects.create(name=name)
        category.save()
        """ RETURN RESPONSE """
        return Response(data=ProductSerializers(category).data)


@api_view(['GET', 'POST'])
def review_list_api_view(request):
    if request.method == "GET":
        reviews = Review.objects.all()
        data_dict = ReviewSerializers(reviews, many=True).data
        return Response(data=data_dict)
    elif request.method == "PUT":
        """ READ BODY """
    text = request.data.get('text')
    product = request.data.get('product')
    stars = request.data.get('stars')
    """ CREATE REVIEW """
    review = Review.objects.create(text=text, product=product, stars=stars)
    review.save()

    """ RETURN RESPONSE """
    return Response(data=ReviewSerializers(review).data)


@api_view(['GET', 'PUT', 'DELETE'])
def category_detail_api_view(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(data={'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data_dict = CategorySerializers(category, many=False).data
        return Response(data=data_dict)
    elif request.method == 'PUT':
        category.name = request.data.get('name')
        category.save()
        return Response(status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail_api_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(data={'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data_dict = ProductSerializers(product, many=False).data
        return Response(data=data_dict)
    elif request.method == 'PUT':
        product.title = request.data.get('title')
        product.description = request.data.get('description')
        product.price = request.data.get('price')
        product.category_id = request.data.get('category_id')
        product.save()
        return Response(status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': 'Review not found'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data_dict = ReviewSerializers(review, many=False).data
        return Response(data=data_dict)
    elif request.method == 'PUT':
        review.text = request.data.get('text')
        review.stars = request.data.get('stars')
        review.product_id = request.data.get('product_id')
        review.save()
        return Response(status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
